const landmarks = JSON.parse(document.getElementById("map-data").textContent);

const map = L.map("map-container").setView([38.9404, -92.3277], 15);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

const markerMap = {};

landmarks.forEach((landmark) => {
  const marker = L.marker([landmark.lat, landmark.lng])
    .addTo(map)
    .bindPopup(`<strong>${landmark.name}</strong><br>${landmark.description}`);
  markerMap[landmark.name] = marker;
});

document.querySelectorAll(".landmark-item").forEach((item) => {
  item.addEventListener("click", () => {
    const marker = markerMap[item.querySelector("strong").textContent];
    if (marker) {
      map.setView(marker.getLatLng(), 17);
      marker.openPopup();
    }
  });
});
