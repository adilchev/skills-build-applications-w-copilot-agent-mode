import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Fetching from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Fetched teams:', data);
        setTeams(Array.isArray(data) ? data : data.results || []);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [apiUrl]);

  return (
    <div>
      <h2>Teams</h2>
      <ul>
        {teams.map((team, idx) => (
          <li key={team.id || idx}>{JSON.stringify(team)}</li>
        ))}
      </ul>
    </div>
  );
};

export default Teams;
