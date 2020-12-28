# Author: CryosisOS
# Date Created: 2020-12-28
# Description:

from flask import Flask, jsonify
from flask import request
from discord.ext import commands
from objects import APICommands


class API:
    def __init__(self, discord_api: commands.Bot):
        self.app = Flask(__name__)
        self.discord_api = discord_api
        self.command_handler = APICommandHandler(self.discord_api)
        self.register_routes()

    def register_routes(self):
        @self.app.route('/execute_command', methods=["POST"])
        def command_handler():
            RESPONSE_ERROR = jsonify(isError=True,
                                     message="Request FAILED due to request body",
                                     statusCode=400), 400
            RESPONSE_FAILED = jsonify(isError=True,
                                      message="Request Failed due to command failure",
                                      statusCode=400), 400
            RESPONSE_SUCCESS = jsonify(isError=False,
                                       message="Successful execution of command",
                                       statusCode=200), 200
            data = request.get_json()
            command_valid = command_handler.validate_api_command_request(data)
            if not command_valid:
                return RESPONSE_ERROR
            valid_args = command_handler.validate_api_command_args(data)
            if not valid_args:
                return RESPONSE_ERROR
            command = data["command"]
            args = data["args"]
            command_success = command_handler.parse_command(command=command, args=args)
            if not command_success:
                return RESPONSE_FAILED
            return RESPONSE_SUCCESS

    def start_server(self):
        self.app.run(port=3000, debug=True)


class APICommandHandler:
    def __init__(self, discord_api: commands.Bot):
        self.discord_api = discord_api
        self.commands: dict = APICommands.initialise_api_commands(self.discord_api)

    def parse_command(self, command: str, args: str):
        return self.commands[command].do_option(args)

    def validate_api_command_request(self, request_data):
        command = request_data["command"]
        if command is None or self.commands.get(command, default=None) is None:
            return False
        return True

    def validate_api_command_args(self, request_data):
        command = request_data["command"]
        args = request_data["args"]
        # Assumed that command exists if this method is called
        if args is not None and self.commands.get(command).requires_args() is True:
            return True
        return False
