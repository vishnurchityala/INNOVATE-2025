import pandas as pd

# Load the Excel file
df = pd.read_excel('leaderboard.xlsx')

# Sort the dataframe by points in descending order
df = df.sort_values(by='Points', ascending=False)

# Generate HTML body content
html_body_content = '''
<div class="cards">
'''

rank_classes = ['rank-first', 'rank-second', 'rank-third']

# Iterate through the dataframe and generate HTML content
for index, row in df.iterrows():
    rank = row['Rank']
    rank_class = rank_classes[rank - 1] if rank <= 3 else ''
    html_body_content += f'''
        <div class="card">
            <div class="rank {rank_class}">{rank}</div>
            <div class="team-name">{row['Team Name']}</div>
            <div class="points">{row['Points']}</div>
        </div>
    '''

html_body_content += '''
</div>
'''

# Save the HTML body content to a file
with open('output_body.html', 'w') as file:
    file.write(html_body_content)
