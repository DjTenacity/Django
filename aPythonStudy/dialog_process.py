from data_utils import data_utils
from intention_model_script import intention_model_bert

class processDialog(object):

	def __init__(self):
		self.batch_size = 10
		self.num_hidden_units = 30

		self.my_utils = data_utils()

		self.intention_model = intention_model_bert.Intention_Classification(
			batch_size=self.batch_size, num_hidden_units=self.num_hidden_units,
			max_utt_len=self.my_utils.max_utt_len, class_num=self.my_utils.class_num)

		self.intention_model.restore()

	#### 解析输入的意图，返回意图值和相应的概率
	def predict_intention(self, utterance):
		u = [self.my_utils.bertWord2id[c] if c in self.my_utils.bertWord2id else self.my_utils.bertWord2id['[UNK]'] for c in utterance]
		u_l = len(u)
		mask = [0] * self.my_utils.max_utt_len
		for m in range(u_l):
			mask[m] = 1

		u = u + [self.my_utils.bertWord2id['[PAD]']] * (self.my_utils.max_utt_len - u_l)

		pred, prob = self.intention_model.forward_bert(
			[u], [mask], [u_l])

		return pred[0], prob[0]

	def read_ori_file(self, ori_fn):
		with open(ori_fn) as fp:
			lines = [line.strip() for line in fp.readlines()]
		my_dict = {line.split()[0]:line.split()[1] for line in lines}
		return my_dict
	##############################################################################
	def start(self, respondant_id=1):

		self.respondant_id = respondant_id

		# convenient: 该人现在是否方便
		# person_stat： 这个电话是否是这个人的
		# intention： 意图
		# call_again： 是否要跟进
		# next_time： 什么时候再打
		self.slot = {'convenient': '',
					 'person_stat': '',
					 'intention': '',
					 'call_again': '',
					 'next_time': '',
					 }

		self.intention = -1

		# 记录上一次的intention
		self.last_intention = -1

		self.byebye_count = 0

		self.need_reply = False

		# last_reply 记录上一句机器回答的话
		self.last_reply = '这样的，我是互联网猎头Amy；你现在讲话方便吗？'

		return self.my_utils.reply2id['喂，您好！请问是张XX吗？我是互联网猎头Amy；现在讲话方便吗？']

	def response(self, u):

		# 意图：
		# 		# 0: '确认', 1: '哪里的', 2: '否认',
		# 		# 3: '暂时不方便-等一下', 4: '暂时不方便-下次再打', 5: '犹豫',
		# 		# 6: '询问', 7: '同一个东西', 8: '没有听清', 9: '其他'

		if len(u) < self.my_utils.max_utt_len:
			# intention: 意图, prob：意图的概率
			# predict_intention：意图识别模型API，u为用户输入的句子
			self.intention, prob = self.predict_intention(u)
			# 纠错
			correct_word, editdist = self.my_utils.correct(u)
			if editdist <= 3 and prob[self.intention] < 0.97:
				self.intention, prob = self.predict_intention(correct_word)
		else:
			# 用户输入的句子太长
			self.intention = -1
			prob = [0.0] * self.my_utils.class_num

		# 用户连续输入了2次机器识别不了的话
		if self.byebye_count >= 2:
			return self.my_utils.reply2id['好的，那不好意思打扰了，再见！']

		# 没听清，重复上一句话
		if self.intention == 8 and prob[self.intention] >= 0.8:
			return self.my_utils.reply2id[self.last_reply]

		# 下次再打，询问时间
		if self.last_intention == 4 and self.need_reply == False:
			self.slot['next_time'] += u
			return self.my_utils.reply2id['好的，我先加你微信，到时候电话联系！']

		# 候选人不方便的情况
		if (self.intention == 3 or self.intention == 4) and prob[self.intention] >= 0.75:
			self.slot['person_stat'] = 1
			self.slot['convenient'] = 0
			self.slot['call_again'] = 1
			self.last_intention = self.intention

			if self.intention == 3:
				self.last_reply = '这样，我三分钟后再打给你，你先忙'
				return self.my_utils.reply2id['好的，不着急，那我三分钟后打给你']
			if self.intention == 4:
				self.last_reply = '你什么时间比较方便？我们可以再电话沟通的。'
				return self.my_utils.reply2id['那你今天几点比较方便？我们可以再电话沟通。']

		# 用户询问问题，或者询问哪里
		elif (self.intention == 6 or self.intention==1) and prob[self.intention] >= 0.7:
			# 如果没有提出不方便，默认用户是方便的
			self.last_intention = self.intention
			self.slot['person_stat'] = 1
			self.slot['convenient'] = 1
			if self.slot['intention'] == '':
				self.need_reply = True
				self.need_slot_key = 'intention'

			# 不让用户一直问问题
			self.byebye_count += 1

			if self.intention == 6:
				self.last_reply = '我是专做互联网的猎头，知道你的联系方式很正常。你近期考虑机会吗？'
				return self.my_utils.reply2id['我这边是专注做互联网的猎头，知道你的联系方式很正常。你近期考虑机会吗？']
			else:
				self.last_reply = '我是专注做互联网的猎头。你近期考虑机会吗？'
				return self.my_utils.reply2id['我这边是专注做互联网的猎头。你近期考虑机会吗？']

		# 需要记录用户非intention的自由对话，但不能增加byebye_count，打开need_reply
		if self.need_reply == True:
			if (self.intention == 0 or self.intention == 2) and prob[self.intention] >= 0.82:
				self.need_reply = False
				if self.need_slot_key == 'intention' and self.intention == 0:
					self.slot[self.need_slot_key] = '考虑'
					return self.my_utils.reply2id['好的，收到。那我让相关同事联系你']
				if self.need_slot_key == 'intention' and self.intention == 2:
					return self.my_utils.reply2id['好的，那不好意思打扰了，再见！']

		# 开始填充 slot
		# 先确认电话号码对不对
		if self.slot['person_stat'] == '':

			if self.intention == 0 and prob[self.intention] >= 0.7:
				# 如果没有提出不方便，默认用户是方便的
				self.last_intention = self.intention
				self.slot['person_stat'] = 1
				self.slot['convenient'] = 1

				# 这里开启了need_reply, 让用户自由说话
				self.need_reply = True
				self.need_slot_key = 'intention'
				self.last_reply = '你最近有在找一些外部机会吗'
				return self.my_utils.reply2id['你最近有在看一些外部机会吗？']

			# 用户否认
			elif self.intention == 2 and prob[self.intention] >= 0.7:
				self.last_intention = self.intention
				self.slot['person_stat'] = 0
				return self.my_utils.reply2id['好的，那不好意思打扰了，再见！']

			else:
				self.byebye_count += 1
				return self.my_utils.reply2id['不好意思，我没有听清，能否再说一遍']

		# 确认用户是否方便
		# cc 要么有空， 要么在说其他东西
		if self.slot['convenient'] == '':
			if self.intention == 0 and prob[self.intention] >= 0.7:
				self.last_intention = self.intention
				self.slot['convenient'] = 1
				self.need_long_reply = True
				self.need_slot_key = 'intention'

				return self.my_utils.reply2id['那你这边倾向考虑什么公司什么方向的机会呢？']
			else:
				self.byebye_count += 1
				return self.my_utils.reply2id['不好意思，我没有听清，能否再说一遍']

		return self.my_utils.reply2id['不好意思，我没有听清，能否再说一遍']

##################################################################################################
if __name__ == "__main__":
	dialog_session = processDialog()
	reply_id = dialog_session.start()
	print(dialog_session.my_utils.id2reply[reply_id])
	while True:
		u = input('')

		if u == 'break':
			break

		reply_id = dialog_session.response(u)

		if reply_id == -1:
			continue

		print(dialog_session.my_utils.id2reply[reply_id])

		if reply_id in list(range(10, 20)):
			print(dialog_session.slot)
			break