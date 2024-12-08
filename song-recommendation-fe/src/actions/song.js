'use server';

const { redirect } = require("next/navigation");
import axios from "axios";

async function song(formData) {
    const song = formData.get("song");
    const response = await axios.post('http://127.0.0.1:8000/find_similar_songs', {
        song_name: song
    });
    const playlist = response.data.playlist_url;
    return redirect(playlist);
}

export default song;