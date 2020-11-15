# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from datetime import  datetime, timedelta
from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted,FollowupAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import datetime

def get_last_utter_action(tracker):
    # follow up for no. of rooms/room type
    for event in reversed(tracker.events):
        try:
            if event.get('name') == 'utter_room_confirmation':
                return
            if event.get('name') in ['utter_no_of_rooms','utter_room_type']:
                return event.get('name')
        except:
            continue

class ActionSetRooms(Action):

    def name(self) -> Text:
        return "action_set_rooms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        room = tracker.get_slot("no_rooms")
        return [SlotSet("no_rooms", room)]

class ActionRoomType(Action):
    
    def name(self) -> Text:
        return "action_room_type"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        room_type = tracker.get_slot("type_room")
        return [SlotSet("type_room", room_type)]

class ActionBookCleanTime(Action):
    def name(self) -> Text:
        return "action_book_clean_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        clean_time = tracker.get_slot("clean_time")
        if clean_time == "now":
            msg = "Sure, I will send someone to your room right away."
        else:
            clean_time = int(clean_time) + datetime.datetime.now().hour
            if clean_time > 12: 
                cleantime = str(clean_time - 12) + " pm"
            else: 
                clean_time = str(clean_time) + " am"
            msg = "Sure, I have scheduled a cleaning for "+str(clean_time)+" today."
        dispatcher.utter_message(msg)
        return [SlotSet("clean_time", tracker.get_slot("clean_time"))]

class ActionCheckIn(Action):
    
    def name(self):
        return "action_check_in"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_check_in")
        return [FollowupAction(get_last_utter_action(tracker))]

class ActionCheckOut(Action):
    
    def name(self):
        return "action_check_out"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_check_out")
        return [FollowupAction(get_last_utter_action(tracker))]

class ActionCancelReservation(Action):
    
    def name(self):
        return "action_cancel_reservation"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_cancel_reservation")
        return [FollowupAction(get_last_utter_action(tracker))]

class ActionCancellationPolicy(Action):
    
    def name(self):
        return "action_cancellation_policy"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_cancellation_policy")
        return [FollowupAction(get_last_utter_action(tracker))]

class ActionRestaurant(Action):
    
    def name(self):
        return "action_restaurant"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_restaurant")
        return [FollowupAction(get_last_utter_action(tracker))]

class ActionBreakfastAvailability(Action):
    
    def name(self):
        return "action_breakfast_availability"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_breakfast_availability")
        return [FollowupAction(get_last_utter_action(tracker))]

class ActionBreakfastTimings(Action):
    
    def name(self):
        return "action_breakfast_timings"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_breakfast_timings")
        return [FollowupAction(get_last_utter_action(tracker))]

class ActionRestaurantTimings(Action):
    
    def name(self):
        return "action_restaurant_timings"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_restaurant_timings")
        return [FollowupAction(get_last_utter_action(tracker))]

class ActionOutofScope(Action):
    def name(self):
        return "action_out_of_scope"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_out_of_scope")
        return [FollowupAction(get_last_utter_action(tracker))]