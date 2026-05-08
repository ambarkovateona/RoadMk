const BASE = 'http://localhost:8001'

export const getReports = (filters = {}) => {
  const params = new URLSearchParams(filters)
  return fetch(`${BASE}/reports?${params}`).then(r => r.json())
}

export const getSummary = () =>
  fetch(`${BASE}/summary`).then(r => r.json())

export const getReport = (id) =>
  fetch(`${BASE}/reports/${id}`).then(r => r.json())
