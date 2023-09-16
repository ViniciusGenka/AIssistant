<h1 align="center">
  <br>
  <a><img src="https://imgur.com/jLUEdMQ.png" alt="AIssistant" width="500"></a>
</h1>

<h4 align="center">A virtual assistant based on ChatGPT</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#use-cases">Use Cases</a> •
  <a href="#how-to-configure">How To Configure</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#support">Support</a> •
  <a href="#license">License</a>
</p>

## Key Features

- Voice-based interactions
  - Ask ChatGPT via voice
  - Get ChatGPT responses directly in your ears
- Time-saver
  - Just a word away
  - Use your clipboard, including in your question pertinent texts such as error logs or code snippets
  - Keeps context of the preceding interactions (customizable)

## Use Cases

- Self Development
  - Practice conversation in any language you want to learn
  - Practice for interviews, debates, negotiations or any communication skills
  - Practicality when studying
- Faster Development and Debugging
  - Ask questions based on code snippets or error logs (using clipboard and voice commands)

## How To Configure

1. Open the config.ini file in a text editor of your preference.
2. Set your OpenAI and Picovoice access keys
3. Set the parameters based on tests and what suits you best

> **Note:**
> if speech recognition is slow or won't finish, consider testing different values on the following parameters: <br>
> • input_energy_threshold: minimum audio energy to be considered speech <br>
> • input_voice_pause_threshold: seconds of silence needed to conclude a question <br>
> • input_adjust_for_ambient_noise: automatic adjustment of the energy threshold, accounting for ambient noise, until a phrase starts <br>
> • input_dynamic_energy_threshold: automatic adjustment of the energy threshold, accounting for ambient noise, in real time <br>

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/). From your command line:

```bash
# Clone this repository
$ git clone https://github.com/ViniciusGenka/AIssistant.git

# Go into the repository
$ cd AIssistant

# Install dependencies
$ pip install -r requirements.txt

# Configure your access keys and the other parameters within the config.ini file
# Run the AIssistant.py file
$ python src/main.py
```

> **Note:**
> you must have two access keys: one from [OpenAI](https://platform.openai.com/docs/introduction) for ChatGPT integration, and another from [Picovoice](https://console.picovoice.ai/) for using wake words.

## Support

<a href="https://www.buymeacoffee.com/vinigenka" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/purple_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## License

MIT

---
