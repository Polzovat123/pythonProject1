from mango_connector import connect_and_push_to_dataset_data

def use_mango_connector(title, link, link_web_site, id, image='not found'):
    connect_and_push_to_dataset_data(title, id, link, link_web_site, image, get_dict_thems(title))

def analysis_text():
    pass

def get_dict_thems(title):
    analysis_text()
    ans = {
        'politic':1,
        'medicine':0
    }
    return ans