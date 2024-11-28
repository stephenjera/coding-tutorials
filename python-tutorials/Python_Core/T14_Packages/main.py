# Import from formats subpackage
from sound.formats.wavread import read_wav
from sound.effects.echo import apply_echo
from sound.filters.equalizer import set_equalizer

# Test each function
def main():
    print(read_wav())         # Expected output: "Reading WAV file"
    print(apply_echo())       # Expected output: "Applying echo effect"
    print(set_equalizer())    # Expected output: "Setting equalizer"

if __name__ == "__main__":
    main()
