class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Creates the defaults for the instance variables.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turns the Tv on and off.
        """
        if not self.__status:
            self.__status = True
        else:
            self.__status = False
            self.__muted = True

    def mute(self)-> None:
        """
        Mutes and unmutes the Tv when it's on.
        """
        if not self.__muted:
            self.__muted = True
        else:
            self.__muted = False

    def channel_up(self) -> None:
        """
        Increases the Tv channel by one when it's on. If this method is called when at the
        maximum value of channels, the Tv will return to the minimum.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases the Tv channel by one when it's on. If this method is called when at
        the minimum value of channels, the Tv will return to the maximum.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases the Tv volume by one when it's on. If this method is called when at
        the maximum value of volumes, the Tv will stay there.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the Tv volume by one when it's on. If this method is called when at
        the minimum value of volumes, the Tv will stay there.
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Gives the user the current values of the Tv variables.
        :return: the current values of the Tv variables
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
