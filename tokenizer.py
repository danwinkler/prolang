import re

class NoneState:
	def handle( self, chars ):
		if chars[0] == " " or chars[0] == "\n":
			return WhiteSpaceState()
		elif re.match( "//", chars ):
			return CommentState()
		elif re.match( "[a-zA-Z][a-zA-Z0-9_]*", chars ):
			return VariableState()
		elif re.match( "[\+\=\-\*\/]", chars ):
			return OperatorState()
		elif re.match( "[0-9]", chars ):
			return NumberState()
		elif chars[0] == ";":
			return EndStatementState()
		elif chars[0] == "(":
			return OpenParenState()
		elif chars[0] == ")":
			return ClosedParenState()

class WhiteSpaceState:
	def handle( self, chars ):
		if chars[0] == " " or chars[0] == "\n":
			return self
		else:
			return NoneState()

class CommentState:
	def handle( self, chars ):
		if chars[0] != "\n":
			return self
		else:
			return NoneState()

class VariableState:
	def handle( self, chars ):
		if re.match( "[a-zA-Z][a-zA-Z0-9_]*", chars ):
			return self
		else:
			return NoneState()

class OperatorState:
	def handle( self, chars ):
		if re.match( "[\+\=\-\*\/]", chars ):
			return self
		else:
			return NoneState()

class NumberState:
	def handle( self, chars ):
		if re.match( "[0-9]", chars ):
			return self
		else:
			return NoneState()

class EndStatementState:
	def handle( self, chars ):
		if chars[0]== ";":
			return self
		else:
			return NoneState()
			
class OpenParenState:
	def handle( self, chars ):
		return NoneState()
			
class ClosedParenState:
	def handle( self, chars ):
			return NoneState()

def tokenize( program ):
	list = []
	current = ""
	state = NoneState()
	i = 0
	while i < len( program ):
		print program[i]
		new_state = state.handle( program[i:] )
		if not isinstance( new_state, NoneState ):
			current += program[i]
			i += 1
		else:
			if not isinstance( state, WhiteSpaceState ):
				list.append( current )
			current = ""
			
		state = new_state
	return list