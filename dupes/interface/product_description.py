import streamlit as st
from streamlit_navigation_bar import st_navbar
from streamlit_card import card
import requests

import streamlit as st

with st.container():

    st.title('PRODUCT DESCRIPTION')
    st.caption("""## Let us know what you're looking for in your new shampoo and we will find affordable options.""", width="stretch", text_alignment="left")

    nlp_text = st.text_input('### Type in the cell below your description.', placeholder="frizz control, hydration, volume, repair?")




if nlp_text:
    params = dict(description=nlp_text)

    # TODO: Change the api URL to google after the test in local

    dupes_web_api = "http://127.0.0.1:8000/recommend"
    dupes_web_api_price = "http://127.0.0.1:8000//recommend_with_price"
    response = requests.get(dupes_web_api,params=params)
    response_price = requests.get(dupes_web_api_price,params=params)

    predictions = response.json()

    predict_price = response_price.json()

    st.markdown("""
                ### No ads. No sponsored brands. Just unbiased recommendations.
                """)

    for prediction in predictions:
        if prediction["product_name"]:


            with st.container(border= True):
                st.title(f"{list(prediction["product_name"].values())[0]}")
                st.caption(f"{list(prediction["en_description"].values())[0]}")
                st.caption(f"Actual price in stores: €{list(prediction["price_eur"].values())[0]} for {list(prediction["volume_ml"].values())[0]} ml.")
                st.caption(f"The price we think its fair: € {round(predict_price['prediction'][0]['price_prediction'],2)} per {predict_price['prediction'][0]['volume_ml']} ml.")






    #     card(
    #         title=f"{list(prediction["product_name"].values())[0]}",
    #         text=[f"{list(prediction["description"].values())[0]}",\
    #                 f"Actual price in stores: €{list(prediction["price_eur"].values())[0]}",\
    #                     f"The price we think its fair: €"],
    #         styles={
    #             "card": {
    #                 "width": "100%",
    #                 "height": "500px",
    #                 "border-radius": "60px",
    #                 "box-shadow": "0 0 10px rgba(0,0,0,0.5)"
    #             },
    #             "text" : {
    #                 "color": "black"
    #             },
    #             "filter": {
    #                 "background-color": "white"
    #             },
    #             "title" : {
    #                 "color": "black"
    #             }
    #             }
    #     )
