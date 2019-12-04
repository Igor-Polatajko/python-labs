function perform_delete(url) {
  fetch(url, {
    method: 'delete'
  }).then(() => window.location.reload())
}

function perform_post(url, data) {
  return fetch(url, {
  headers: {
      'Content-Type': 'application/json'
    },
    method: 'post',
    body: JSON.stringify(data)
  }).then(() => window.location.reload())
}

function perform_put(url, data) {
  return fetch(url, {
  headers: {
      'Content-Type': 'application/json'
    },
    method: 'put',
    body: JSON.stringify(data)
  }).then(() => window.location.reload())
}