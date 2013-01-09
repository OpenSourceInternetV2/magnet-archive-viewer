
# A search result
class Result(object):
	def __init__(self, name, magnet, size, se, le):
		# Result info
		self.name = name
		self.magnet = magnet
		self.size = size
		self.se = se
		self.le = le


class Search(object):
	def __init__(self, file_name):
		self.file_name = file_name

	def search(self, term):
		# Open database
		f = open(self.file_name, 'r')

		result_list = []

		print 'Performing search...'
		for line in f:
			line = line[:-1]

			# Split the line
			parts = line.split('|')
			name = parts[1]
			
			# If there's no hash (happens sometimes),
			# ignore the result
			magnet = parts[-1]
			if magnet == '':
				continue

			le = int(parts[-2])
			se = int(parts[-3])
			size = int(parts[-4])

			# If there's a search with more than one
			# word, eg. "David Bowie", we should split
			# "David" and "Bowie" and search for both
			# terms anywhere in the name
			terms = term.lower().split(' ')

			# Lowercase everything
			name_lower = name.lower()

			# If all the terms are in the name, add the result
			# to the result list
			if all(t in name_lower for t in terms):
				result_list.append(Result(name, magnet, size, se, le))

		f.close()

		print 'Done!'

		print 'Sorting by seed count...'
		result_list.sort(key=lambda r: r.se, reverse=True)
		print 'Done!'

		return result_list
