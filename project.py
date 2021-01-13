import pandas as pd
import psycopg2
import streamlit as st
from configparser import ConfigParser

'# The Internet Archive '

@st.cache
def get_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    return {k: v for k, v in parser.items(section)}


@st.cache
def query_db(sql: str):
    print(f'Running query_db(): {sql}')

    db_info = get_config()
    print("test1")
    # Connect to an existing database
    print(db_info)
    conn = psycopg2.connect(**db_info)
    print("test2")

    # Open a cursor to perform database operations
    cur = conn.cursor()
    print("test3")
    # Execute a command: this creates a new table
    cur.execute(sql)

    # Obtain data
    data = cur.fetchall()
    print(data) 
    column_names = [desc[0] for desc in cur.description]

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()

    df = pd.DataFrame(data=data, columns=column_names)

    return df

'## Choose and view from all memes:'
sql_meme_names = 'select * from meme;'
meme_names = query_db(sql_meme_names)['subject'].tolist()
meme_name = st.selectbox('Choose a meme', meme_names)
if meme_name:
    sql_meme = f"select * from meme full outer join personality_posts on personality_posts.meme_id=meme.id where subject = '{meme_name}';"
    meme_info = query_db(sql_meme).loc[0]
    meme_content = meme_info['content']
    author = meme_info['name']
    if author is not None:
        st.write(f"{author} posted:")
    st.image(meme_content, caption=None, use_column_width=True, channels='RGB')

'## See which meme communities internet personalities belong to:'
sql_personality_names = 'select * from internet_personality;'
personality_names = query_db(sql_personality_names)['name'].tolist()
personality_name = st.selectbox('Select personality', personality_names)
if personality_name:
    personality = f"select * from internet_personality full outer join personality_belongs_to_subculture on internet_personality.name = personality_belongs_to_subculture.name where internet_personality.name = '{personality_name}';"
    personality_info = query_db(personality).loc[0]
    subculture = personality_info['subculture_name']
    person = personality_info['name']
    if subculture is not None:
        st.write(f"{personality_name} is a part of {subculture}.")
    else:
        st.write(f"{personality_name} is a part of no subculture.")


'## See which real life communities internet personalities belong to:'
sql_personality_names = 'select * from internet_personality;'
personality_names = query_db(sql_personality_names)['name'].tolist()
personality_name = st.selectbox('Select community ', personality_names)
if personality_name:
    personality = f"select * from internet_personality full outer join personality_belongs_to_community on internet_personality.name = personality_belongs_to_community.name where internet_personality.name = '{personality_name}';"
    personality_info = query_db(personality).loc[0]
    community = personality_info['real_life_community_name']
    person = personality_info['name']
    if community is not None:
        st.write(f"{personality_name} is a part of {community}.")
    else:
        st.write(f"{personality_name} is a part of no community.")


'## List memes by aesthetic'
sql_aesthetics = 'select *  from meme_has_an;'
aesthetics= query_db(sql_aesthetics)['aesthetic_name'].tolist()
aesthetic_sel = st.radio('Choose an aesthetic', aesthetics)
if aesthetic_sel:
    sql_memes = f"select subject, content from meme join meme_has_an on meme.id=meme_has_an.meme_id where aesthetic_name = '{aesthetic_sel}';"
    meme_content = query_db(sql_memes)['subject'].tolist()
    meme_content_str = '\n\n'.join([str(elem) for elem in meme_content])
    st.write(f"These memes have an {aesthetic_sel} aesthetic.\n\n {meme_content_str}")

'## List memes from a given source'
sql_sources = 'select *  from source;'
sources= query_db(sql_sources)['website'].tolist()
source_sel = st.radio('Choose a source', sources)
if source_sel:
    sql_sources = f"select subject, content from meme join meme_posted_on on meme.id=meme_posted_on.meme_id where source_website = '{source_sel}';"
    meme_content = query_db(sql_sources)['subject'].tolist()
    meme_content_str = '\n\n'.join([str(elem) for elem in meme_content])
    st.write(f"These memes came from {source_sel}.\n\n {meme_content_str}")

'## List memes from a given era'
sql_eras = 'select *  from era;'
eras= query_db(sql_eras)['name'].tolist()
era_sel = st.radio('Choose an era', eras)
if era_sel:
    sql_eras = f"select subject, content from meme join meme_in_era on meme.id=meme_in_era.meme_id where era_name = '{era_sel}';"
    meme_content = query_db(sql_eras)['subject'].tolist()
    meme_content_str = '\n\n'.join([str(elem) for elem in meme_content])
    st.write(f"These memes came from the {era_sel} era.\n\n {meme_content_str}")

