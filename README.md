# bmtc
*download requirements.txt*
pip3 install -r requirements.txt

*download selenium latest version*
sudo pip3 install selenium

*download latest firefox browser*
sudo apt-get install firefox

*download latest geckodriver, untar it, make it executable and put it in path usr/local/bin*
wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo cp ./geckodriver /usr/local/bin

*run the program*
python3 bmtc.py
