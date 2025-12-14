const Activities = () => {
  const [activities, setActivities] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;

  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setActivities(results);
        console.log('Fetched activities:', results);
      })
      .catch(err => console.error('Error fetching activities:', err));
  }, [endpoint]);

  return (
    <div className="card p-4">
      <h2 className="card-title mb-3">Activities</h2>
      <div className="table-responsive">
        <table className="table table-striped table-bordered">
          <thead>
            <tr>
              <th>#</th>
              <th>Activity</th>
              <th>Date</th>
              <th>Details</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity, idx) => (
              <tr key={activity.id || idx}>
                <td>{activity.id || idx + 1}</td>
                <td>{activity.name || activity.type || '-'}</td>
                <td>{activity.date || activity.created_at || '-'}</td>
                <td><pre className="mb-0">{JSON.stringify(activity, null, 2)}</pre></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Activities;
