def calculate_spacings(total_width, material_width_min, material_width_max = None):
    master_spacing_dict = {} # Defining the master dictonary
    

    for material_width in range(material_width_min, material_width_max + 1 if material_width_max != None else material_width_min + 1): # Sets the range for the material widths if you want to use a range. If you provide 1 argument to the function, It will instead set the max = to the minimum value + 1 and run only one time.
        
        for pieces in range(1, total_width // material_width + 1): # The main loop. Runs through pieces in a range of 1(skip 0) to the total width(ex. 1024)/ current mwidth(ex. 64) + 1 The + 1 allows for the range to reach the upper limit since it only goes to 64, but does not include it.
            spaces = pieces + 1 # If you have 3 pieces in an opening, you have 4 spaces. Universal math.
            
            spacing = (total_width - (material_width * pieces)) / (spaces) # The math I learned as a finish carpenter
            # you can always check your results by taking the spacing(ex. 208)
            # * the # spaces(ex. 4 since 3 pieces) 208 x 4 = 832
            # + (matwidth(ex. 64) * 3 pieces) 64 x 3 =      +192
            # addition                                      1024

            if spacing.is_integer(): # The only main conditional. Ignores decimal numbers completely
                spacing_info = {     # Creates a dict of information to be appended to the current keys empty list that is about to be made/ already is made.
                    "Pieces": pieces,
                    "Spacing": int(spacing)
                }
                if f"Material Width: {material_width}" not in master_spacing_dict: # This is mostly for formatting. if (ex. "Width: 3") is not made.  
                    master_spacing_dict[f"Material Width: {material_width}"] = []  # It makes it as an empty list inside the Master Dict as the value
                master_spacing_dict[f"Material Width: {material_width}"].append(spacing_info)# Appends the spacing information dict current widths list value. 
    return master_spacing_dict # the end    


# Display results
def print_result(spacing_results): # A lot of trial and error went into formatting the tables correctly. 
                                   # I don't need to explain this. It prints the tables.
                                   # The jist is, It makes an string, and appends carefully and dynamically constructed formatting.  
    for mat_width, spacings in spacing_results.items(): # master dict
        columns = " | Pieces |  | Spacing |"
        print_statement = (f"{mat_width}\n{columns}\n " + ("-" * (len(columns) - 1)) + "\n") # Adds columns, and a dashed seperator based on the length of the columns

        for spacing_infos in spacings:
            for key, value in spacing_infos.items():
                spaces = " " * ((len(key)+ 1) - len(str(value))) # dynamically adding spaces to the string based on the len of the keys so that the seperators form a line
                print_statement += f" | {value}{spaces}| "
                
            print_statement += "\n"   
        print(print_statement + "\n")   

# Define the parameters: A kind of redundant function since you could just plug everything into calculate spacings.
# I do enjoy the clarity for the user should they open the code.
def mainP(tw, mtm, mtx = None):
    total_width = tw  # For clarity  not actually doing anything
    material_width_min = mtm
    material_width_max = mtx

    # Calculate spacings
    spacing_results = calculate_spacings(total_width, material_width_min, material_width_max )
    
    print_result(spacing_results) # Display results
mainP(1024, 16,32)

# How to use:
    # The first number is the total width of your opening
    # The second number is the minimum size of the material you want to be centered 
    #** The third number is the maximum size of the material and is optional.
    #** If you do not add the third number, the program will give you results from the single minimum value
    # This program only returns whole numbers. Nothing is rounded. Decimal numbers are discarded as they serve no purpose in keeping brushes on grid. 



#Todo: 
# Error handeling? Probably not.
# UI? Probably not 
# If I do one, I might aswell do both.