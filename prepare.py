import pandas as pd
import nltk
import re

image_extensions = ['jpg', 'png', 'gif']
def detect_image(url):
        split = url.split('.')
        return (split[len(split)-1] in image_extensions)


submission_data = pd.read_csv('test_output.csv')

submission_data['is_image'] = submission_data['url'].apply(lambda x: detect_image(x))
submission_data.drop(columns=['url','index'],inplace=True)
submission_data.index.rename('index',inplace=True)


file = submission_data.to_csv("cleaned_submissions.csv")