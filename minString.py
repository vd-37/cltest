def getMinString(s: str) -> str:
    # Repeat the process until no changes are made
    while True:
        changed = False  # Flag to check if any change happened in the current loop
        
        # Try replacing each possible triplet (substring of length 3) with "100"
        for i in range(len(s) - 2):
            # Generate a new string by replacing the substring starting at index i with "100"
            modified_string = s[:i] + "100" + s[i+3:]
            
            # Check if the new string is lexicographically smaller
            if modified_string < s:
                s = modified_string  # Update the string with the new one
                changed = True  # Mark that a change happened
                break  # Restart the process since a change was made
        
        # If no changes were made, break out of the loop
        if not changed:
            break
    
    return s
