import os
from moviepy.editor import VideoFileClip

def mp4_to_mp3_converter():
    print("MP4 to MP3 Converter")
    
    # Input MP4 file
    while True:
        input_file = input("Enter the path to your MP4 file: ")
        if os.path.isfile(input_file) and input_file.lower().endswith('.mp4'):
            break
        else:
            print("Invalid file path or not an MP4 file. Please try again.")
    
    # Output MP3 file
    output_file = input("Enter the desired name for your MP3 file (without extension): ") + ".mp3"
    
    try:
        # Load the video file
        video = VideoFileClip(input_file)
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to an MP3 file
        audio.write_audiofile(output_file)
        
        # Close the video file
        video.close()
        
        print(f"Conversion complete! MP3 file saved as: {output_file}")
    
    except Exception as e:
        print(f"An error occurred during conversion: {str(e)}")

if __name__ == "__main__":
    mp4_to_mp3_converter()
