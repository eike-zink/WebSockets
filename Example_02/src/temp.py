    async for message in websocket:
        # Pars a `play` event from the UI
        event = json.loads(message)
        assert event['type'] == 'play'
        column = event['column']
        # Get the row
        try:
            # Play the move
            row = game.play(player, column)
        except RuntimeError as exc:
            # Send an `error` event it the move was illegal
            event = {
                'type': 'error',
                'message': str(exc)
            }
            await websocket.send(json.dumps(event))
            continue
        # Send a `play` event to update the UI
        event = {
            'type': 'play',
            'player': player,
            'column': column,
            'row': row
        }
        await websocket.send(json.dumps(event))
        # If move is winning, send a `win` event
        if game.winner is not None:
            event = {
                'type': 'win',
                'player': game.winner
            }
            await websocket.send(json.dumps(event))
        # Alternate turns
        player = next(turns)