const Teams = () => {
  const [teams, setTeams] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Fetched teams:', results);
      })
      .catch(err => console.error('Error fetching teams:', err));
  }, [endpoint]);

  return (
    <div className="card p-4">
      <h2 className="card-title mb-3">Teams</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead>
            <tr>
              <th>#</th>
              <th>Team Name</th>
              <th>Members</th>
              <th>Details</th>
            </tr>
          </thead>
          <tbody>
            {teams.map((team, idx) => (
              <tr key={team.id || idx}>
                <td>{team.id || idx + 1}</td>
                <td>{team.name || '-'}</td>
                <td>{Array.isArray(team.members) ? team.members.length : '-'}</td>
                <td><pre className="mb-0">{JSON.stringify(team, null, 2)}</pre></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Teams;
