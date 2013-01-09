
class Result(object):
	def __init__(self, name, magnet, size, se, le):
		self.name = name
		self.magnet = magnet
		self.size = size
		self.se = se
		self.le = le


class Search(object):
	def __init__(self, file_name):
		self.file_name = file_name

	def search(self, term):
		f = open(self.file_name, 'r')

		result_list = []

		print 'Performing search...'
		for line in f:
			line = line[:-1]

			parts = line.split('|')
			name = parts[1]
			
			#print line
			
			magnet = parts[-1]
			if magnet == '':
				continue

			#print 'hash! <' + magnet + '>'

			le = int(parts[-2])
			se = int(parts[-3])
			size = int(parts[-4])

			terms = term.lower().split(' ')

			name_lower = name.lower()

			if all(t in name_lower for t in terms):
				result_list.append(Result(name, magnet, size, se, le))

		f.close()

		print 'Done!'

		print 'Sorting by seed count...'
		result_list.sort(key=lambda r: r.se, reverse=True)
		print 'Done!'

		return result_list
