DATASET = [
    # answer is a ground truth, that can be compared with the response from model to calculate the correctness.
    {
        "question": "How do I activate seat heating?",
        "relevant": "To activate seat heating, press the seat heating button on the center console.",
        "distractor": "The air conditioning system automatically adjusts cabin temperature.",
        "answer": "Press the seat heating button on the center console."
    },

    {
        "question": "How do I turn on the headlights?",
        "relevant": "Headlights can be activated using the light switch on the dashboard.",
        "distractor": "The infotainment system provides access to media and navigation.",
        "answer": "Use the light switch on the dashboard."
    },

    {
        "question": "How do I open the trunk?",
        "relevant": "The trunk can be opened by pressing the trunk release button on the key fob or driver door.",
        "distractor": "The fuel door is located on the rear side of the vehicle.",
        "answer": "Press the trunk release button on the key fob or driver door."
    },

    {
        "question": "How do I activate cruise control?",
        "relevant": "Cruise control is activated using the control lever on the steering wheel.",
        "distractor": "The brake system ensures safe stopping of the vehicle.",
        "answer": "Use the control lever on the steering wheel."
    },

    {
        "question": "How do I adjust the side mirrors?",
        "relevant": "Side mirrors can be adjusted using the mirror adjustment switch on the driver door.",
        "distractor": "Seat position can be adjusted using controls on the side of the seat.",
        "answer": "Use the mirror adjustment switch on the driver door."
    },

    {
        "question": "How do I turn on the windshield wipers?",
        "relevant": "Windshield wipers are controlled using the wiper stalk on the steering column.",
        "distractor": "The rear window defroster removes fog from the back window.",
        "answer": "Use the wiper stalk on the steering column."
    },

    {
        "question": "How do I activate parking assist?",
        "relevant": "Parking assist can be activated by pressing the parking assist button on the center console.",
        "distractor": "Navigation guidance is displayed on the central screen.",
        "answer": "Press the parking assist button on the center console."
    },

    {
        "question": "How do I lock the doors?",
        "relevant": "Doors can be locked using the lock button on the key fob or driver door.",
        "distractor": "Interior lighting can be adjusted through the settings menu.",
        "answer": "Use the lock button on the key fob or driver door."
    },

    {
        "question": "How do I start the engine?",
        "relevant": "The engine is started by pressing the start/stop button while pressing the brake pedal.",
        "distractor": "The battery provides power to electrical components.",
        "answer": "Press the start/stop button while pressing the brake pedal."
    },

    {
        "question": "How do I activate steering assist?",
        "relevant": "Steering assist can be activated using the button on the steering wheel.",
        "distractor": "Blind spot monitoring alerts the driver to nearby vehicles.",
        "answer": "Press the steering assist button on the steering wheel."
    },

    # EDGE CASE 1 (heating vs cooling)
    {
        "question": "How do I cool the car?",
        "relevant": "The air conditioning system can be activated using the climate control panel.",
        "distractor": "Seat heating warms the seats during cold conditions.",
        "answer": "Use the climate control panel to activate air conditioning."
    },

    # EDGE CASE 2 (similar control location confusion)
    {
        "question": "How do I activate the windshield wipers?",
        "relevant": "Windshield wipers are controlled using the wiper stalk on the steering column.",
        "distractor": "Cruise control is operated using a lever on the steering wheel.",
        "answer": "Use the wiper stalk on the steering column."
    }

]