import operator

INITIAL = (3, 3, 0)
GOAL = (0, 0, 1)


class Status:
	def __init__(self, cannibals, missionaries, boat):
		self.state = (missionaries, cannibals, boat)
		self.cannibals = cannibals
		self.missionaries = missionaries
		self.boat = boat

	def is_legal(self):
		if self._has_more_cannibals():
			return False
		elif self._has_more_boats():
			return False
		else:
			return True

	def is_goal(self):
		if self.state == (0, 0, 1):
			return True
		else:
			return False

	def _has_more_cannibals_left(self):
		return ((self.missionaries == 1 and self.cannibals == 3) or
				(self.missionaries == 1 and self.cannibals == 2) or
				(self.missionaries == 2 and self.cannibals == 3))

	def _has_more_cannibals_right(self):
		return ((self.missionaries == 1 and self.cannibals == 0) or
				(self.missionaries == 1 and self.cannibals == 0))

	def _has_more_cannibals(self):
		return self._has_more_cannibals_left() or self._has_more_cannibals_right()

	def _has_more_boats(self):
		return self.boat > 1

	def __add__(self, other):
		result = tuple(map(operator.add, self.state, other))
		return Status(result[0], result[1], result[2])

	def __sub__(self, other):
		result = tuple(map(operator.sub, self.state, other))
		return Status(result[0], result[1], result[2])

	def __str__(self):
		return '<Status {}>'.format(self.state)

	def __eq__(self, other):
		return isinstance(other, Status) and self.state == other.state

	def __hash__(self):
		return hash(self.state)


class Solution:
	def __init__(self):
		initial_status = Status(INITIAL[0], INITIAL[1], INITIAL[2])
		goal_status = Status(GOAL[0], GOAL[1], GOAL[2])
		super().__init__(initial_status, goal_status)

	def action(self, status):
		actions = self.get_all_actions()
		return self.get_legal_actions(status, actions)

	def get_legal_actions(self, status, actions):
		is_valid = lambda action: self.operation(status, action)
		return set(filter(is_valid, actions))

	def get_all_actions(self):
		return {
			(1, 0, 1),
			(2, 0, 1),
			(0, 2, 1),
			(1, 1, 1),
			(0, 1, 1)
		}

	def operation(self, status, op):
		do = self.do_operation(status.boat)
		return do(status, op)

	def do_operation(self, boat):
		return operator.sub if boat == 0 else operator.add



def main():
	pass

if __name__ == '__main__':
	main()