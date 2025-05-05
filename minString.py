def getMinString(s):
    # Continue modifying the string until no more changes are possible
    while True:
        changed = False
        
        # Try to modify the string by replacing a substring with "100"
        for i in range(len(s) - 2):
            modified_string = modify_string(s, i)
            
            # If the modified string is lexicographically smaller, update the string
            if is_lexicographically_smaller(modified_string, s):
                s = modified_string
                changed = True
                break  # Restart the loop since a change was made
        
        # Exit if no changes were made in this iteration
        if not changed:
            break
    
    return s

# Helper Method 1: Modify the string by replacing a substring with "100"
def modify_string(s, i):
    return s[:i] + "100" + s[i+3:]

# Helper Method 2: Check if a string is lexicographically smaller than another string
def is_lexicographically_smaller(modified_string, original_string):
    return modified_string < original_string
