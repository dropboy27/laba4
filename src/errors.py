class NotEnoughMoneyError(Exception):
    def __init__(self, player_name, balance, required):
        self.player_name = player_name
        self.balance = balance
        self.required = required
        message = f"У {player_name} недостаточно денег: есть {balance}, нужно {required}"
        super().__init__(message)
