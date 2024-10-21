
// const availableSlots = {{ doctor["available_slots"] | tojson | safe }} ;
    
//     // Doctor's current appointments (with booked dates and slots)
// const doctorAppointments = {{ appointments | tojson | safe }};
const available_slots = document.getElementById("available_slots").value;
console.log(available_slots) ;
const doctor_appointments = document.getElementById("appointments").value;
console.log(doctor_appointments) ;
const availableSlots = JSON.parse(available_slots) ;
console.log(availableSlots);

const doctorAppointments = JSON.parse(doctor_appointments);
console.log(doctorAppointments);

document.getElementById("appointment-date").addEventListener("change", function () {
  
  var selectedDate = this.value;  // selected from calender
  var slotSelect = document.getElementById("slot");
  slotSelect.innerHTML = '<option value="">Select a slot</option>';

  
  var bookedSlots = doctorAppointments
    .filter(function(appointment) {          //(filter)return true if appointment with same date as selected date
      return appointment.date === selectedDate;
    })
    .map(function(appointment) {  //(map) create array with filtered appointmets
      return appointment.slot;
    });

  
  availableSlots.forEach(function(slot) {
    if (bookedSlots.indexOf(slot) === -1) {  // If the slot is not in bookedSlots
      var option = document.createElement("option");
      option.value = slot;
      option.textContent = slot;
      slotSelect.appendChild(option);
    }
  });
});
