import json
import os
from dotenv import load_dotenv

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Load environment variables from .env file
load_dotenv()

# Retrieve API key and URL from environment variables
apikey = os.environ['apikey']
url = os.environ['url']

# Create IAMAuthenticator instance using API key
authenticator = IAMAuthenticator(apikey)

# Create LanguageTranslatorV3 instance using authenticator and service URL
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates English text to French using IBM Watson Language Translator.
    """
    # Translate English text to French
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    # Extract translated text in French from the response
    french_text = translation['translations'][0]['translation']
    
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using IBM Watson Language Translator.
    """
    # Translate French text to English
    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    # Extract translated text in English from the response
    english_text = translation['translations'][0]['translation']

    return english_text