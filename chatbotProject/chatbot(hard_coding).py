chatbot = [
    [
        ["greetings"],
        [
            "hello",
            "good afternoon",
            "can you help me?",
            "good morning",
            "good evening",
            "hi",
            "hey",
            "what's up?",
            "how are you?"
        ],
        [
            "Hello there!",
            "Hi, how may I help you?",
            "What can I help you with?"
        ]
    ],

    ############## TEMPLATE ##############
    [
        ["topic"],
        [
            "add the first possible user input",
            "add the second possible user input",
            "add the third possible user input",
        ],
        [
            "add the first possible chatbot response",
            "add the second possible chatbot response",
            "add the third possible chatbot response"
        ]
    ]
]

from datasets import load_dataset

ds = load_dataset("stanfordnlp/coqa")