## greet + book + 1_no_rooms + simple_room_type

* greet
  - utter_greet

* book_room
  - utter_no_of_rooms

* inform_no_rooms{"no_rooms":"1"}
  - action_set_rooms
  - slot{"no_rooms":"1"}
  - utter_room_type

* inform_room_type{"type_room":"simple"}
  - action_room_type
  - slot{"type_room":"simple"}
  - utter_room_confirmation

* thanks
  - utter_welcome

* goodbye
  - utter_goodbye

## greet + book + 1_no_rooms + deluxe_room_type

* greet
  - utter_greet

* book_room
  - utter_no_of_rooms

* inform_no_rooms{"no_rooms":"1"}
  - action_set_rooms
  - slot{"no_rooms":"1"}
  - utter_room_type

* inform_room_type{"type_room":"deluxe"}
  - action_room_type
  - slot{"type_room":"deluxe"}
  - utter_room_confirmation

* thanks
  - utter_welcome

* goodbye
  - utter_goodbye

## greet + book + 2_no_rooms + simple_room_type

* greet
  - utter_greet

* book_room
  - utter_no_of_rooms

* inform_no_rooms{"no_rooms":"2"}
  - action_set_rooms
  - slot{"no_rooms":"2"}
  - utter_room_type

* inform_room_type{"type_room":"simple"}
  - action_room_type
  - slot{"type_room":"simple"}
  - utter_room_confirmation

* thanks
  - utter_welcome

* goodbye
  - utter_goodbye

## greet + book + 2_no_rooms + deluxe_room_type

* greet
  - utter_greet

* book_room
  - utter_no_of_rooms

* inform_no_rooms{"no_rooms":"2"}
  - action_set_rooms
  - slot{"no_rooms":"2"}
  - utter_room_type

* inform_room_type{"type_room":"deluxe"}
  - action_room_type
  - slot{"type_room":"deluxe"}
  - utter_room_confirmation

* thanks
  - utter_welcome

* goodbye
  - utter_goodbye

<!-- No. of Rooms specified in the same sentence -->

## greet + 1_no_rooms + simple_room_type

* greet
  - utter_greet

* book_room{"no_rooms":"1"}
  - action_set_rooms
  - slot{"no_rooms":"1"}
  - utter_room_type

* inform_room_type{"type_room":"simple"}
  - action_room_type
  - slot{"type_room":"simple"}
  - utter_room_confirmation

* thanks
  - utter_welcome

* goodbye
  - utter_goodbye

## greet + 1_no_rooms + deluxe_room_type

* greet
  - utter_greet

* book_room{"no_rooms":"1"}
  - action_set_rooms
  - slot{"no_rooms":"1"}
  - utter_room_type

* inform_room_type{"type_room":"deluxe"}
  - action_room_type
  - slot{"type_room":"deluxe"}
  - utter_room_confirmation

* thanks
  - utter_welcome

## greet + 2_no_rooms + simple_room_type

* greet
  - utter_greet

* book_room{"no_rooms":"2"}
  - action_set_rooms
  - slot{"no_rooms":"2"}
  - utter_room_type

* inform_room_type{"type_room":"simple"}
  - action_room_type
  - slot{"type_room":"simple"}
  - utter_room_confirmation

* thanks
  - utter_welcome

## greet + 2_no_rooms + deluxe_room_type

* greet
  - utter_greet

* book_room{"no_rooms":"2"}
  - action_set_rooms
  - slot{"no_rooms":"2"}
  - utter_room_type

* inform_room_type{"type_room":"deluxe"}
  - action_room_type
  - slot{"type_room":"deluxe"}
  - utter_room_confirmation

* thanks
  - utter_welcome

<!-- Clean Room -->
## clean the room + Right now

* greet
  - utter_greet

* clean_room
  - utter_arrange_cleaning

* inform_time_clean{"clean_time":"now"}
  - action_book_clean_time
  - slot{"clean_time":"now"}

* thanks
  - utter_welcome

## clean the room + after_1_hr

* greet
  - utter_greet

* clean_room
  - utter_arrange_cleaning

* inform_time_clean{"clean_time":"1"}
  - action_book_clean_time
  - slot{"clean_time":"1"}

* thanks
  - utter_welcome

## clean the room + after_2_hr

* greet
  - utter_greet

* clean_room
  - utter_arrange_cleaning

* inform_time_clean{"clean_time":"2"}
  - action_book_clean_time
  - slot{"clean_time":"2"}

* thanks
  - utter_welcome

* goodbye
  - utter_goodbye

## clean the room + after_3_hr

* greet
  - utter_greet

* clean_room
  - utter_arrange_cleaning

* inform_time_clean{"clean_time":"3"}
  - action_book_clean_time
  - slot{"clean_time":"3"}

* thanks
  - utter_welcome

* goodbye
  - utter_goodbye

## clean the room + after_5_hr

* greet
  - utter_greet

* clean_room
  - utter_arrange_cleaning

* inform_time_clean{"clean_time":"5"}
  - action_book_clean_time
  - slot{"clean_time":"5"}

* thanks
  - utter_welcome