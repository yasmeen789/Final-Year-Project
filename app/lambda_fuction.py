"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6
For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Name and date of birth"
                    # "Welcome to your child companion setup. "\
                    # "Please tell me the name and date of birth of the child "\
                    # " that will be using this application."\
                    # " For example, my child's name is "\
                    # "Scarlet and her date of birth is the 21st September 2003."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me the name and date of birth of the child "\
                    " that will be using this application."\
                    " For example, my child's name is "\
                    "Scarlet and her date of birth is the 21st September 2003."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using your child's companion. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_childs_name_attributes(childs_name):
    return {"childsName": childs_name}

def create_date_of_birth(date_of_birth):
    return {"dateOfBirth": date_of_birth}

def create_month_of_birth(month_of_birth):
    return {"monthOfBirth": month_of_birth}

def create_year_of_birth(year_of_birth):
    return {"yearOfBirth": year_of_birth}

def set_childs_details_in_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Child' in intent['slots']:
        childs_name = intent['slots']['Child']['value']
        session_attributes = create_childs_name_attributes(childs_name)
        if 'Date' in intent['slots']:
            date_of_birth = intent['slots']['Date']['value']
            session_attributes = create_date_of_birth(date_of_birth)
            if 'Month' in intent['slots']:
                month_of_birth = intent['slots']['Month']['value']
                session_attributes = create_month_of_birth(month_of_birth)
                if 'Year' in intent['slots']:
                    year_of_birth = intent['slots']['Year']['value']
                    session_attributes = create_year_of_birth(year_of_birth)
        speech_output = "Your child's name is " + childs_name + \
                        ", and their date of birth is the " \
                        + date_of_birth + " of " + month_of_birth + \
                        year_of_birth + ". Is this true or false?"
        reprompt_text = "Your child's name is " + childs_name + \
                        ", and their date of birth is the " \
                        + date_of_birth + " of " + month_of_birth + \
                        year_of_birth + ". Is this true or false?"
    else:
        speech_output = "I'm not sure what your child's name is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your child's name is. " \
                        "Please tell me the name and date of birth of the child "\
                        " that will be using this application."\
                        " For example, my child's name is "\
                        "Scarlet and her date of birth is the 21st September 2003."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def create_confirm_details_attributes(confirm_details):
    return {"confirmDetails": confirm_details}

def set_confirm_details_from_session(intent, session):
    """ Sets the confirm in the session and prepares the speech to reply to the
    user.
    """
    session_attributes = {}
    reprompt_text = None

    card_title = intent['name']
    session_attributes = {}

    if 'ConfirmDetails' in intent['slots']:
        confirm_details = intent['slots']['ConfirmDetails']['value']
        session_attributes = create_confirm_details_attributes(confirm_details)
        if confirm_details == 'true':
            speech_output = "Setup complete. To begin reading 'The Gruffalo '"\
                            "by Julia Donaldson, say start."
            should_end_session = False
        elif confirm_details == 'false':
            speech_output = "Please tell me the name and date of birth of the child "\
                            " that will be using this application."\
                            " For example, my child's name is "\
                            "Scarlet and her date of birth is the 21st September 2003."
            should_end_session = False
        else:
            speech_output = "I don't know what you said"
    else:
        speech_output = "I'm not sure what your child's name is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your child's name is. " \
                        "Please tell me the name and date of birth of the child "\
                        " that will be using this application."\
                        " For example, my child's name is "\
                        "Scarlet and her date of birth is the 21st September 2003."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_request_start_reading(intent, session):
    session_attributes = {}
    reprompt_text = None

    speech_output = "You have requested to start reading the Gruffalo."
    # audio goes here
    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MyChildsNameIsIntent":
        return set_childs_details_in_session(intent, session)
    elif intent_name == "ConfirmChildsNameIntent":
        return set_confirm_details_from_session(intent, session)
    elif intent_name == "StartIntent":
        return start_instructions(intent, session)
    elif intent_name == "AMAZON.NextIntent":
        return get_next(intent, session)
    elif intent_name == "AMAZON.PauseIntent":
        return set_pause(intent, session)
    elif intent_name == "AMAZON.ResumeIntent":
        return get_repeat(intent, session)
    elif intent_name == "StartReadingBook":
        return get_request_start_reading(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
