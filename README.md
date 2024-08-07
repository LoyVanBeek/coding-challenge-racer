# Coding Challenge: Multiplayer Racing Game [![Python application](https://github.com/Rayman/coding-challenge-racer/actions/workflows/python-app.yml/badge.svg)](https://github.com/Rayman/coding-challenge-racer/actions/workflows/python-app.yml)

![Demo](./demo.gif)

## Description

The goal is to build a bot that is faster than all other bots.

You should write your bots logic in a Python class.
Each frame, the `update` method of your bot will be called with the current state of the game and the bot should return the desired action to take.

There is one example bot implemented: [SimpleBot](https://github.com/nobleans-playground/coding-challenge-racer-bot-template/blob/main/bot.py).
You can use that repository as starting point for your bot.
Read [How to submit a bot](#how-to-submit-a-bot) to learn how to get started.

## How to run the game

On the command line, go to the folder where you have cloned this repository and run the following command:
```bash
python3 -m racer
```

## Game rules

1. The exact rules of the game are implemented in [racer/game_state.py](./racer/game_state.py).
2. You must go through each waypoint in the track in the correct order.
   The track is a closed loop, so after the last waypoint you have to drive again over the first one.
3. The bot that completes 3 rounds on the track first wins.

## Tournament rules

1. You are allowed to submit a maximum of two bots.
2. Your bot must be your own creation.
   This rule is so that you may not blatantly copy someone's bot, change only a few lines, and then submit it as your own.
   *Some* code duplication is of course inevitable and thus allowed, because the logic might be similar between bots.
   You are allowed to use AI tools to help you create your bot.
3. The code of the game is law.
   The rules of the game are implemented in the code.
   If you want to know the specific rules of the game, please look at the code.
   If the game determines you've won a game, that is the outcome.
4. Please limit the processing time of your bot.
   Currently, there's a hard limit of `16ms` _average_ time-per-frame as measured by [tournament.py](./tournament.py).
   Please talk to one of the organizers if you think this is too short.
   You can also use a profiler to try and make your code faster.
5. You can only use the Python libraries that are in the [requirements.txt](./requirements.txt) file.
   If you want to use another library, please let one of the organizers know.
6. Multithreading is not allowed
7. You are not allowed to read or alter the game's internal state, or the state of other bots.
   You can only use the information that is given via the interface.
   You are allowed to import the game's classes and use them in your bot.

## How to submit a bot

Your bot will live as a git submodule inside the main challenge repository.
This means you will need to create your own GitHub account and create a new repository based on a template.
You can follow the following steps to create your own bot.

**Note**: You are allowed to submit a maximum of two bots.

1. Create a GitHub account if you don't have one already.
   Using a personal account is fine.
2. Create a personal repository where your bot will live.
   You can do this by clicking the "Use this template" button in [this repo](https://github.com/nobleans-playground/coding-challenge-racer-bot-template), or by forking the repository.
3. Give your bot a name and add your own name as contributor
   Notify an organizer @Rayman or @heinwessels to add your bot to the challenge as a submodule in the main repository.
   Note: Your bot doesn't have to be complete to be added, it simply needs to run and return a valid move.
   You can update/change/refactor your bot at any point during the challenge.
   Use this template" in  to create your own bot repository.
