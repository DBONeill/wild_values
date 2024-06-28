import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#########
# SETUP #
#########
intro_text = """
Are you concerned about the loss of nature and wildlife? Do you think society should be taking action to protect nature before it’s too late?    

If your answer to both of these questions is “yes” then you’re one of many. Most people in the UK are concerned about the loss of nature and wildlife. Most of us agree that nature needs to be protected, but we have many different views about how and why we should go about doing this.
If we want the same outcomes for nature but have different views about how to achieve those outcomes, then it’s important that we try to understand our own views more completely. It’s surely even more important that we try to understand the views of others. There is no one way to protect nature, just like there is no one way to deliver public services, and no one way to organise society. 

When it comes to issues like organising society, we have long-established ways to measure and understand our views—like whether we’re on the left or the right politically. The same cannot be said for of nature and its protection. Are there distinct ways of thinking about nature and how to protect it? Do these relate to different the different values we hold?
These are the questions we’re hoping you’ll enjoy helping us answer.
"""

# Define the statements and sub-scales
questions = {
    "1. Valuation": [
        "Putting a price on nature could lead to it being harmed",
        "Putting a monetary value on nature gives conservation greater priority in policy choices",
        "Putting a monetary value on nature helps to protect it",
        "Putting a value on nature gives it better protection in political and economic decision-making",
        "It is morally wrong to put a price on nature",
        "Other economic priorities will always overshadow conservation, regardless of whether nature has a monetary value"
    ],
    "2. Wildness": [
        "The main role of conservation should be to remove human influences from unhealthy landscapes (e.g., fences, powerlines, dams) and allow nature to take its course",
        "The goal of conservation should be to restore environments to what they would've been before humans modified them and keep them that way",
        "A landscape managed and controlled by people cannot be called 'natural'",
        "Attempts to manage nature lead to its degradation",
        "Wild nature can only be restored by ceasing human interference",
        "Conservation should aim to convert managed landscapes into wild ones"
    ],
    "3. Capitalism": [
        "Only by working with businesses will conservation receive enough funding to protect nature",
        "Conservation can be effective without the support of businesses",
        "Conservation should not have to compromise by working with businesses to protect nature",
        "Protecting nature will be less successful if nature organisations attempt to leverage businesses to their advantage",
        "To protect nature, conservation should embrace opportunities to work with businesses",
        "Governments alone don’t have the financial capacity or resources to look after nature"
    ],
    "4. Science": [
        "Local knowledge is more useful than science when looking after nature",
        "Nature can only be protected when decisions are based on science",
        "Decisions about how to care for nature should be based on facts and not opinion",
        "Decisions about how to look after nature should never be based on just science",
        "Science is just a small part of helping us decide how to look after nature",
        "People need science to help protect nature"
    ],
    "5. Animals": [
        "Animals should have rights similar to the rights of people",
        "The things done to protect nature should not cause any animal to suffer",
        "Hunting should not be part of looking after nature because it harms individual animals",
        "Taking care of individual animals is less important than looking after nature as a whole",
        "Sometimes it is ok to do things that harm animals to protect the natural world (e.g., killing animals that are damaging woodlands)"
    ],
     "6. People": [
        "Local people should have the greatest say in looking after nature",
        "Work to look after nature should aim to improve access to nature for all",
        "Disadvantaged people should have a say in how nature is looked after",
        "It’s ok for people to be inconvenienced in order to conserve nature",
        "Work to care for nature should have nothing to do with people's wellbeing",
        "Focus on people’s wellbeing can undermine efforts to look after nature"
    ]
}

sub_scale_descriptions = {
    "1. Valuation": """<div style="font-size: 24px; font-weight: bold; text-align: left;">The Bumble Bee / Wild Economist</b> 🐝 </div><p></p>

   <div style="font-size: 16px; text-align: left;"><p>Wild Economists see the benefits of valuing nature in monetary terms.</p>

<p>A high score in the Valuation scale indicates a strong belief that putting a price on nature is important for its protection.</p>
<p>17 percent of Wildlife Trust supporters are Wild Economists, scoring highest or joint-highest on the Valuation scale.</p>
<p>You might be interested in conservation initiatives such as <a href=" https://www.ywt.org.uk/how-do-you-restore-degraded-peatland" target="_blank">Yorkshire Wildlife Trust’s peatland restoration</a> and writers like <a href="https://tonyjuniper.com/" target="_blank">Tony Juniper</a>, who has written books on ecosystem services.</p>
</div>""",
    "2. Wildness":"""<div style="font-size: 24px; font-weight: bold; text-align: left;">The Lynx / Wilderness Advocate</b> 🐈</div><p></p>
    <div style="font-size: 16px; text-align: left;"><p>Wilderness Advocates have a preference for wild and unmanaged landscapes versus management-intensive conservation.</p>
    <p>A high score on the Wildness scale suggests you favour minimal human intervention in natural landscapes, and favour rewilding-based approaches to conservation.</p>
    <p>12 percent of Wildlife Trust supporters are Wilderness Advocates, scoring highest or joint-highest on the Wildness scale. This is the rarest type among supporters.</p>
    <p>You might be interested in conservation initiatives such as <a href=" https://www.missinglynxproject.org.uk/" target="_blank">The Missing Lynx Project</a>, the documentary <a href="https://www.wildingmovie.com/" target="_blank">Wilding</a> and writers like <a href="https://en.wikipedia.org/wiki/Aldo_Leopold" target="_blank">Aldo Leopold</a>.</p>     
 </div>""",
    "3. Capitalism": """<div style="font-size: 24px; font-weight: bold; text-align: left;">The Ant / Nature Entrepreneur</b> 🐜 </div><p></p>
<div style="font-size: 16px; text-align: left;"><p>Nature Entrepreneurs tend to believe that businesses can play an important role in conservation.</p>
<p>A high score on the Capitalism scale suggests you believe that businesses should play a significant role in protecting nature.</p>
<p>21 percent of Wildlife Trust supporters are Nature Entrepreneurs, scoring highest or joint-highest on the Capitalism scale.</p>
<p>You might be interested in conservation initiatives such as the <a href="https://www.wildlifetrusts.org/atlantic-rainforest-restoration" target="_blank">Atlantic Rainforest Restoration Programme</a> and <a href="https://www.cornwallwildlifetrust.org.uk/news/seasalt-partners-cornwall-wildlife-trust-pioneering-seagrass-restoration-project" target="_blank">Cornwall Wildlife Trust’s seagrass restoration project</a>.</p>    
</div>""",
    "4. Science": """<div style="font-size: 24px; font-weight: bold; text-align: left;">The Dolphin / Wild Scientist</b> 🐬</div><p></p>
<div style="font-size: 16px; text-align: left;">
<p>Wild Scientists value scientific knowledge and methods in conservation. A high score on the Science scale indicates a strong preference on science for making conservation decisions.</p>
<p>17 percent of Wildlife Trust supporters are Wild Scientists, scoring highest or joint-highest on the Science scale.</p>
<p>You might be interested in the work of biological records centres, such as <a href="https://www.surreywildlifetrust.org/what-we-do/professional-services/records-centre" target="_blank">Surrey Wildlife Trust’s</a>, writers like <a href="https://en.wikipedia.org/wiki/E.O._Wilson" target="_blank">E.O. Wilson</a> and documentaries such as <a href="https://theendofthelinemovie.com/" target="_blank">The End of The Line</a>.</p>    
</div>""",
    "5. Animals":"""<div style="font-size: 24px; font-weight: bold; text-align: left;">The Octopus / Compassionate Protector</b> 🐙 </div><p></p>
<div style="font-size: 16px; text-align: left;">
<p>Compassionate Protectors prioritise the rights of animals in conservation. A high score reflects a strong concern for animal welfare in conservation efforts.</p>
<p>31 percent of Wildlife Trust supporters are Compassionate Protectors, scoring highest or joint-highest on the Animals scale. This is the most common type among supporters.</p>
<p>You might be interested in the work of many organisations to <a href="https://squirrelaccord.uk/news/blog/press-notice-grey-squirrel-fertility-control-research-hits-key-milestone/" target="_blank">manage grey squirrels compassionately</a> and philosophers like <a href="https://en.wikipedia.org/wiki/Peter_Singer" target="_blank">Peter Singer</a>.</p>
</div>""",
    "6. People":"""<div style="font-size: 24px; font-weight: bold; text-align: left;">The Oak / Wild Egalitarian</b> 🌳 </div><p></p>
<div style="font-size: 16px; text-align: left;">
<p>Wild Egalitarians prioritise the benefits to people in conservation work. A high score suggests that you regard the access and involvement of local communities in conservation work as particularly important.</p>
<p>15 percent of Wildlife Trust supporters are Wild Egalitarians, scoring highest or joint-highest on the People scale.</p>
<p>You might be interested in The Wildlife Trusts’ <a href="https://www.wildlifetrusts.org/nextdoor-nature" target="_blank">Nextdoor Nature Project</a> and writers like <a href="https://en.wikipedia.org/wiki/Richard_Louv" target="_blank">Richard Louv</a>.</p>
</div>"""
}



#######################
## Read in WT data:   #
#######################
d = pd.read_csv('scores.csv')

# Rename columns
d = d.rename(columns={'Valuation': '1. Valuation', 'Wildness': '2. Wildness',
                      'Capitalism': '3. Capitalism', 'Science': '4. Science', 'Animals': '5. Animals', 'People': '6. People'})

# Calculate averages (could use some/all of these to display traces)
avs = d.mean()
q1 = d.quantile(0.25)
q3 = d.quantile(0.75)
median = d.median()

# Prepare data for plots
categories = avs.index.tolist()
values = avs.values.tolist()

# Define the labels and corresponding values for the slider
slider_labels = ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"]
slider_values = [0, 1, 2, 3, 4]

# Define reverse coding map for each item
reverse_coding_map = {
    "1. Valuation": [0, 4, 5],
    "2. Wildness": [],
    "3. Capitalism": [1, 2, 3],
    "4. Science": [0, 3, 4],
    "5. Animals": [3, 4], 
    "6. People": [3, 4, 5]
}

################################
# Initialise the Streamlit app #
################################

# Initialize session state variables
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'intro'

if 'responses' not in st.session_state:
    st.session_state.responses = {category: [None] * len(items) for category, items in questions.items()}

# Sidebar
with st.sidebar:
    st.image('./logo.png')
    st.markdown(
        f"""
        <div style="text-align: justify; word-wrap: break-word;">
                By taking the Wild Values test, we’re inviting you to explore your relationship to nature,
                and to share your views on protecting nature. There are no correct answers to any of the questions.
                The questions are opportunities to think about the how and why of protecting nature.
        </div>
        """,
        unsafe_allow_html=True
    )

# Define function to handle navigation
def go_to_section(section):
    st.session_state.current_section = section



# Display sections based on current state
if st.session_state.current_section == 'intro':
    st.title("The Wild Values Test")
    st.markdown(intro_text)
    st.button('Start the Test', on_click=go_to_section, args=('test',))

elif st.session_state.current_section == 'test':
    st.title("The Wild Values Test")
    st.header("Questions")
    for category, items in questions.items():
        st.header(category)
        for idx, item in enumerate(items):
            reverse_code = idx in reverse_coding_map[category]
            response = st.select_slider(
                item, options=range(len(slider_labels)), 
                value=slider_labels.index("Neutral"), 
                format_func=lambda x: slider_labels[x], key=f"{category}_{idx}"
            )
            if reverse_code:
                response = 4 - response
            st.session_state.responses[category][idx] = response
    st.button('View Results', on_click=go_to_section, args=('results',))

################
# RESULTS PAGE #
################
elif st.session_state.current_section == 'results':
    st.title("Results")
    st.header("Your Wild Values personality type is:")
    responses = st.session_state.responses
    raw_scores = {category: sum(responses[category]) for category in responses}
    normalized_scores = {}
    
    # TABLE AND SCORE CALCULATION
    for category, raw_score in raw_scores.items():
        max_raw_score = len(questions[category]) * 4
        min_raw_score = 0
        normalized_score = ((raw_score - min_raw_score) / (max_raw_score - min_raw_score)) * 100
        normalized_scores[category] = int(normalized_score)
    
    sub_scale_df = pd.DataFrame(list(normalized_scores.items()), columns=["Category", "Score"])

    # Calculate the difference between the user's score and the average score
    differences = {category: normalized_scores[category] - avs[category] for category in normalized_scores}
    highest_diff_category = max(differences, key=differences.get)
    highest_diff_value = differences[highest_diff_category]

    # Insert detailed description for the highest difference category
    highest_diff_description = sub_scale_descriptions[highest_diff_category]
    st.markdown(f"<div style='text-align: center; font-size: 16px;'>{highest_diff_description}</div>", unsafe_allow_html=True)

    #st.markdown('<div style="text-align: center;">Your total score for each category:</div>', unsafe_allow_html=True)
    #st.table(sub_scale_df.style.set_table_attributes("class='centered'"))
    df = pd.DataFrame([normalized_scores])

    # CREATE RADAR PLOT AND OTHER RESULTS (IF NORMALIZED SCORES DEFINED)
    if normalized_scores:
        fig = go.Figure()
        # Add all individual traces
        for index, row in d.iterrows():
            fig.add_trace(go.Scatterpolar(
                r=row.values.tolist() + [row.values[0]],
                theta=categories + [categories[0]],  # Ensure consistent order
                mode='lines',
                line=dict(width=1, color='rgba(255,255,255, 0.1)'),  # Set line width and transparency
                hoverinfo='skip'
            ))
        
        # Plot Mean
        fig.add_trace(go.Scatterpolar(
            r=avs.values.tolist() + [avs.values[0]],
            theta=categories + [categories[0]],  # Ensure consistent order
            mode='lines',
            name='Average score',
            fill='toself',
            line=dict(width=3, color='rgba(108, 156, 153, 1)'),  # Solid line for the mean
            hoveron='points+fills',
            fillcolor='rgba(108, 156, 153, 0.7)',
            hovertemplate='Average score: %{r}<br>Dimension: %{theta}<extra></extra>'
        ))
        
        # Plot your result
        fig.add_trace(go.Scatterpolar(
            r=df.iloc[0].values.tolist() + [df.iloc[0].values[0]],
            theta= categories + [categories[0]],  # Ensure consistent order
            mode='lines',
            name='Your score',  
            line=dict(width=3, color='rgba(255, 176, 75, 1)'),  # Solid line for your score
            hoveron='points+fills',
            fillcolor='rgba(255, 176, 75, 0.7)',
            hovertemplate='Your score: %{r}<br>Dimension: %{theta}<extra></extra>'
        ))

        # Update layout of the plot
        fig.update_layout(
            title={
                'text': "How you (orange) compare to the average Wildlife Trust supporter (teal):",
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            title_font_size=20,  # Adjust the font size of the title
            showlegend=False,
            polar=dict(
                bgcolor="lightgrey",
                radialaxis=dict(
                    visible=True,
                    range=[0, 110],  # Assuming the scores are normalized to 0-100
                    tickfont=dict(size=12, color='black')
                ),
                angularaxis=dict(
                    rotation=90,  # Rotate to start from 12 o'clock position
                    direction="clockwise"  # Ensure clockwise direction
                )
            ),
            width=900,  # Specify the width of the plot in pixels
            height=900,
            margin=dict(l=50, r=50, t=100, b=50) 
        )
        
        st.plotly_chart(fig)
    
    # CREATE PANEL OF HISTOGRAMS
    # Initialize a figure with subplots (2 columns, 3 rows)
    fig2 = make_subplots(rows=3, cols=2, subplot_titles=d.columns)

    # Iterate over each column and create a subplot (2 columns, 3 rows)
    for i, col in enumerate(d.columns):
    # Determine the position of the subplot (row, col)
        row = (i // 2) + 1
        col_pos = (i % 2) + 1

        # Create histogram trace
        histogram = go.Histogram(
        x=d[col], 
        name='Data', 
        marker=dict(
            color='rgba(255, 255, 255, 0.9)',
            line=dict(
                color='black',  # Outline color
                width=1      # Outline width
            )
        ),
        xbins=dict(
            start=0,  # Starting point of bins
            end=100,  # End point of bins
            size=5    # Bin width
        )
    )

        # Add histogram trace to the figure
        fig2.add_trace(histogram, row=row, col=col_pos)

        # Get the maximum y value from the histogram
        hist_data = d[col].dropna()
        max_y = hist_data.value_counts(bins=range(0, 105, 5)).max()

        # Set the upper limit for y-axis
        y_max = max_y * 1.3

        # Add a vertical line for the mean score
        fig2.add_vline(
        x=avs[i], 
        line=dict(color='rgba(108, 156, 153, 0.8)', width=7),
        annotation_text=f'Average score: {round(avs[i], 2)}',
        annotation=dict(font=dict(color='rgba(255, 255, 255, 1)', weight='bold', size = 15)),
        annotation_position='top',
        row=row, 
        col=col_pos
        )

        fig2.add_vline(
        x=round(df.iloc[0].values.tolist()[i]), 
        line=dict(color='rgba(255, 176, 75, 0.8)', width=7),
        annotation_text=f'Your score: {round(df.iloc[0].values.tolist()[i], 2)}',
        annotation=dict(font=dict(color='rgba(0, 0, 0, 1)', weight='bold', size = 15)),
        annotation_position='top right',
        row=row, 
        col=col_pos
        )

        # Update the y-axis for the subplot
        fig2.update_yaxes(range=[0, y_max], row=row, col=col_pos)

    # Update layout for the entire figure
    fig2.update_layout(
    title={
                'text': "Your results in detail:",
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
    title_font_size=20,
    xaxis_title='',
    yaxis_title="Frequency",
    bargap=0,      # No gap between bars
    bargroupgap=0, # No gap between groups of bars
    plot_bgcolor='lightgrey',  # Background color of the entire plot
    showlegend=False,          # Do not show legend for individual histograms
    height=1200,               # Set the total height of the figure
    width=1200,                  # Set the width of the figure
    margin=dict(l=50, r=50, t=150, b=50)
    )

    for annotation in fig2['layout']['annotations']:
        if 'Average score' not in annotation['text'] or 'Your score' not in annotation['text']:
            annotation['y'] += 0.03  # Move subplot titles further upwards
        if 'Average score' in annotation['text']:
            annotation['y'] += 0.02  # Move subplot titles further upwards

    # Show the plot
    st.plotly_chart(fig2)

    ## Add a table of all personality types:
    st.header("All Wild Values personality types in detail:")
    for scale, description in sub_scale_descriptions.items():
        st.markdown(f"**{scale}**", unsafe_allow_html=True)
        st.markdown(description, unsafe_allow_html=True)



    
    st.button('Back to Intro', on_click=go_to_section, args=('intro',))