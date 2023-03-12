import pynput
from pynput.keyboard import Key, Listener
import matplotlib.pyplot as plt
import seaborn as sns

keys_pressed = 0
keys = []

def on_press(key):
    global keys, keys_pressed
    keys.append(key)
    keys_pressed += 1
    print("{0} pressed".format(key))

    if keys_pressed >= 1:
        write_file(keys)
        keys = []
        keys_pressed = 0
    

def write_file(keys):
    try:
        with open("log.txt", "a") as f:
            for key in keys:
                k = str(key).replace("'", "")
                f.write(k + '\n')
    except IOError as e:
        print("Error writing to file: ", e)


def on_release(key):
    if key == Key.esc:
        return False

try:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
finally:
    listener.stop()


def count_string_frequencies(file_path):
    string_frequencies = {}
    with open(file_path, 'r') as f:
        for line in f:
            # Split the line into words
            words = line.strip().split()
            # Count the frequency of each word
            for word in words:
                if word in string_frequencies:
                    string_frequencies[word] += 1
                else:
                    string_frequencies[word] = 1
    # Return the dictionary of string frequencies
    return string_frequencies

# Call the count_string_frequencies() function to get the dictionary of string frequencies
string_frequencies = count_string_frequencies('log.txt')

# Convert the dictionary of string frequencies to a 2D array
frequencies = [[string_frequencies.get(key, 0) for key in string_frequencies.keys()]]

# Create the heatmap using the seaborn library
ax = sns.heatmap(frequencies, cmap='Greens', annot=True, fmt='d', square=True, cbar=False, xticklabels=list(string_frequencies.keys()))

# Set the x-axis label rotation to 90 degrees
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

# Add title and axis labels
plt.title('Heatmap of String Frequencies')
plt.xlabel('String')
plt.ylabel('Frequency')

# Show the plot
plt.show()

