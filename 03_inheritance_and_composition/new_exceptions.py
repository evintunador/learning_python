# usually you should use one of the built-in exceptions
# sometimes there's no good match
# sometimes you want to catch one specific thing without risking that some other
# operation will raise teh same exception and be caught by mistake

# there's not much to do here
# pass because python blocks cannot be empty

class GroupValidationError(ValueError):
    pass

# this class would be good for describing a very specific type of ValueError