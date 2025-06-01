import pandas as pd

# Load the CSV file
response_df = pd.read_csv("responses.csv")
score_df = pd.read_csv("score.csv")


# List of keywords to identify STEM majors
stem_keywords = [
    "engineering", "computer", "physics", "chemistry", "biology",
    "math", "mathematics", "data", "science", "biotech", "bio", "neuro"
]

# Filters
stem_mask = response_df["What major are you?"].str.lower().fillna("").apply(
    lambda x: any(keyword in x for keyword in stem_keywords)
)
year_col = response_df['What year are you in?'].str.lower().str.strip()
transfer_col = response_df['Are you a transfer student?'].str.lower().str.strip()
gender_col = response_df['What gender do you identify with?'].str.lower().str.strip()
college_col = response_df['What college are you in?'].str.strip()
jtccer_col = response_df[
    'Have you taken a class that satisfies the Jane Teranes Climate Change Education Requirement (JTCCER)?\nList of Courses'
].str.lower().str.strip()




# Get the indices for different queries
stem_indices = response_df[stem_mask].index.tolist()
non_stem_indices = response_df[~stem_mask].index.tolist()

first_year_indices = response_df[year_col == '1st'].index.tolist()
second_year_indices = response_df[year_col == '2nd'].index.tolist()
third_year_indices = response_df[year_col == '3rd'].index.tolist()
fourth_year_indices = response_df[year_col == '4th'].index.tolist()

transfer_indices = response_df[transfer_col == 'yes'].index.tolist()
non_transfer_indices = response_df[transfer_col == 'no'].index.tolist()

male_indices = response_df[gender_col == 'male'].index.tolist()
female_indices = response_df[gender_col == 'female'].index.tolist()

revelle_indices = response_df[college_col == 'Revelle'].index.tolist()
muir_indices = response_df[college_col == 'Muir'].index.tolist()
marshall_indices = response_df[college_col == 'Marshall'].index.tolist()
warren_indices = response_df[college_col == 'Warren'].index.tolist()
roosevelt_indices = response_df[college_col == 'Roosevelt'].index.tolist()
sixth_indices = response_df[college_col == 'Sixth'].index.tolist()
seventh_indices = response_df[college_col == 'Seventh'].index.tolist()
eighth_indices = response_df[college_col == 'Eighth'].index.tolist()
grad_student_indices = response_df[college_col == "I'm a graduate student."].index.tolist()

jtccer_yes_indices = response_df[jtccer_col == 'yes'].index.tolist()
jtccer_no_indices = response_df[jtccer_col == 'no'].index.tolist()






# Compute the averages of their involvement score
stem_avg = (score_df.loc[stem_indices, "Sum"].sum()) / len(stem_indices)
non_stem_avg = (score_df.loc[non_stem_indices, "Sum"].sum()) / len(non_stem_indices)

first_yr_avg = (score_df.loc[first_year_indices, "Sum"].sum()) / len(first_year_indices)
second_yr_avg = (score_df.loc[second_year_indices, "Sum"].sum()) / len(second_year_indices)
third_yr_avg = (score_df.loc[third_year_indices, "Sum"].sum()) / len(third_year_indices)
fourth_yr_avg = (score_df.loc[fourth_year_indices, "Sum"].sum()) / len(fourth_year_indices)

transfer_avg = (score_df.loc[transfer_indices, "Sum"].sum()) / len(transfer_indices)
non_transfer_avg = (score_df.loc[non_transfer_indices, "Sum"].sum()) / len(non_transfer_indices)

male_avg = (score_df.loc[male_indices, "Sum"].sum()) / len(male_indices)
female_avg = (score_df.loc[female_indices, "Sum"].sum()) / len(female_indices)

revelle_avg = score_df.loc[revelle_indices, "Sum"].mean()
muir_avg = score_df.loc[muir_indices, "Sum"].mean()
marshall_avg = score_df.loc[marshall_indices, "Sum"].mean()
warren_avg = score_df.loc[warren_indices, "Sum"].mean()
roosevelt_avg = score_df.loc[roosevelt_indices, "Sum"].mean()
sixth_avg = score_df.loc[sixth_indices, "Sum"].mean()
seventh_avg = score_df.loc[seventh_indices, "Sum"].mean()
eighth_avg = score_df.loc[eighth_indices, "Sum"].mean()
grad_avg = score_df.loc[grad_student_indices, "Sum"].mean()


jtccer_yes_avg = score_df.loc[jtccer_yes_indices, "Sum"].mean()
jtccer_no_avg = score_df.loc[jtccer_no_indices, "Sum"].mean()



# Print Scores
print(f"STEM Average Involvement Score: {stem_avg:.2f}")
print(f"Non-STEM Average Involvement Score: {non_stem_avg:.2f}")

print(f"First Year Average Involvement Score: {first_yr_avg:.2f}")
print(f"Second Year Average Involvement Score: {second_yr_avg:.2f}")
print(f"Third Year Average Involvement Score: {third_yr_avg:.2f}")
print(f"Fourth Year Average Involvement Score: {fourth_yr_avg:.2f}")

print(f"Transfer Student Involvement Score: {transfer_avg:.2f}")
print(f"Non Transfer Student Involvement Score: {non_transfer_avg:.2f}")

print(f"Male Student Involvement Score: {male_avg:.2f}")
print(f"Female Student Involvement Score: {female_avg:.2f}")


print(f"Revelle Involvement Score: {revelle_avg:.2f}")
print(f"Muir Involvement Score: {muir_avg:.2f}")
print(f"Marshall Involvement Score: {marshall_avg:.2f}")
print(f"Warren Involvement Score: {warren_avg:.2f}")
print(f"Roosevelt Involvement Score: {roosevelt_avg:.2f}")
print(f"Sixth Involvement Score: {sixth_avg:.2f}")
print(f"Seventh Involvement Score: {seventh_avg:.2f}")
print(f"Eighth Involvement Score: {eighth_avg:.2f}")
print(f"Graduate Student Involvement Score: {grad_avg:.2f}")

print(f"People who have taken JTCCER classes Involvement Score: {jtccer_yes_avg:.2f}")
print(f"People who have NOT taken JTCCER classes Involvement Score: {jtccer_no_avg:.2f}")