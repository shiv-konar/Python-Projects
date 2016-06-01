import os.path
import pickle
class TVRemote:
    def __init__(self):
        #self.channel_number = 0
        self.min_channel_number = 0
        self.max_channel_number = 100

        #self.volume = 10
        self.min_volume = 0
        self.max_volume = 100

        self.is_tv_on = True
        self.num_options = 7

        if not os.path.isfile('./savetvstate'):
            self.channel_number = 0
            self.volume = 10
            with open('./savetvstate', 'w') as f:
                pickle.dump([self.channel_number, self.volume], f)
        else:
            with open('./savetvstate', 'r') as f:
                self.channel_number, self.volume = pickle.load(f)

    def display_options(self):
        print "1. Channel (+)"
        print "2. Channel (-)"
        print "3. Jump to channel"
        print "4. Volume (+)"
        print "5. Volume (-)"
        print "6. Mute"
        print "7. OFF"

    def turn_off(self):
        with open('./savetvstate', 'w') as f:
            pickle.dump([self.channel_number, self.volume], f)
        print "TV is turned off."
        self.is_tv_on = False

    def increment_channel(self):
        if self.channel_number == self.max_channel_number:
            self.channel_number = self.min_channel_number
        else:
            self.channel_number += 1
        print '\nYou are watching channel %d\n' % (self.channel_number)

    def decrement_channel(self):
        if self.channel_number == self.min_channel_number:
            self.channel_number = self.max_channel_number
        else:
            self.channel_number -= 1
        print '\nYou are watching channel %d\n' % (self.channel_number)

    def increment_volume(self):
        if self.volume >= self.max_volume:
            self.volume = self.max_volume
            print '\nMax volume.\n'
        else:
            self.volume += 5
        print 'Volume: %d\n' % (self.volume)

    def decrement_volume(self):
        if self.volume <= self.min_volume:
            self.volume = self.min_volume
            print '\nAudio muted. Increase sound to hear audio.\n'
        else:
            self.volume -= 5
        print 'Volume: %d' % (self.volume)

    def mute(self):
        self.volume = self.min_volume
        print '\nAudio muted. Increase sound to hear audio.\n'


    def jump_to_channel(self, channel_number):
        if channel_number > self.max_channel_number:
            print '\nNo such channel. Available channels 0 - 100\n'
        else:
            print '\nYou are watching channel %d\n' %(channel_number)
            self.channel_number = channel_number

    def isvalid_option(self, option):
        if isinstance(int(option), int) and int(option) in range(1, self.num_options + 1):
            return int(option)
        else:
            return 0

print 'TV is ON'
tvremote = TVRemote()
print 'You are watching channel {0}'.format(tvremote.channel_number)
print 'Volume: {0}'.format(tvremote.volume)
while tvremote.is_tv_on:
    tvremote.display_options()

    user_option = raw_input("Your option:")
    try:
        if tvremote.isvalid_option(user_option):
            if int(user_option) == 1:
                tvremote.increment_channel()

            if int(user_option) == 2:
                tvremote.decrement_channel()

            if int(user_option) == 3:
                channel_number = raw_input("Change to channel? ")
                if isinstance(int(channel_number), int):
                    tvremote.jump_to_channel(int(channel_number))

            if int(user_option) == 4:
                tvremote.increment_volume()

            if int(user_option) == 5:
                tvremote.decrement_volume()

            if int(user_option) == 6:
                tvremote.mute()

            if int(user_option) == 7:
                tvremote.turn_off()
        else:
            print '\nInvalid option. Try again.\n'
    except:
        print '\nInvalid option. Try again.\n'

