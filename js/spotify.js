window.onSpotifyWebPlaybackSDKReady = () => {
    const token = 'BQBNe2Po-KJjnhAIJ4_HmAp0m3Q48MAPO2hZJLHi7qZQXOTUWHJjOokV9ZA9X66u51s4P2gUHd4A1nMTIpSUzE8dLBStcVLsArr1EDpOaPO8zBPhOojDP7nAHP2yX4_1lKp7kZm3fh4RU47vYMsovEK40oHGhaoX';
    const player = new Spotify.Player({
      name: 'Web Playback SDK Quick Start Player',
      getOAuthToken: cb => { cb(token); }
    });

    // Error handling
    player.addListener('initialization_error', ({ message }) => { console.error(message); });
    player.addListener('authentication_error', ({ message }) => { console.error(message); });
    player.addListener('account_error', ({ message }) => { console.error(message); });
    player.addListener('playback_error', ({ message }) => { console.error(message); });

    // Playback status updates
    player.addListener('player_state_changed', state => { console.log(state); });

    // Ready
    player.addListener('ready', ({ device_id }) => {
      console.log('Ready with Device ID', device_id);
    });

    // Not Ready
    player.addListener('not_ready', ({ device_id }) => {
      console.log('Device ID has gone offline', device_id);
    });

    // Connect to the player!
    player.connect();
  };