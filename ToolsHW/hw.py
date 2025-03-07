import webbrowser
import sys

def play_video():
    """Opens a YouTube video."""
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    webbrowser.open(video_url)

def main():
    """Prompt user for multiplication answer and play video if correct."""
    while True:
        try:
            user_input = input("1 times 1 = ? (type 'exit' to quit): ")
            if user_input.lower() == "exit":
                sys.exit()
            if int(user_input) == 1:
                print("Correct! Enjoy the video.")
                play_video()
                break
            else:
                print("Wrong! Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
