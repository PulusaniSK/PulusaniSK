import SwiftUI
import PassKit

struct ContentView: View {
    @State private var selectedRocket: String?
    @State private var selectedSeat: String?
    @State private var selectedDestination: String?
    @State private var departureDate = Date()
    @State private var returnDate = Date()
    @State private var numberOfPassengers = 1
    @State private var ticketPrice: Double = 0.0
    @State private var showingConfirmationScreen = false
    
    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Rocket")) {
                    Picker("Select a Rocket", selection: $selectedRocket) {
                        Text("Falcon 9").tag("Falcon 9" as String?)
                        Text("Starship").tag("Starship" as String?)
                        Text("New Shepard").tag("New Shepard" as String?)
                    }
                }
                
                Section(header: Text("Seat")) {
                    Picker("Select a Seat", selection: $selectedSeat) {
                        Text("Economy").tag("Economy" as String?)
                        Text("Business").tag("Business" as String?)
                        Text("First Class").tag("First Class" as String?)
                    }
                }
                
                Section(header: Text("Destination")) {
                    Picker("Select a Destination", selection: $selectedDestination) {
                        Text("Mars").tag("Mars" as String?)
                        Text("Moon").tag("Moon" as String?)
                        Text("Alpha Centauri").tag("Alpha Centauri" as String?)
                    }
                }
                
                Section(header: Text("Dates")) {
                    DatePicker("Departure", selection: $departureDate, in: Date()...)
                    DatePicker("Return", selection: $returnDate, in: departureDate...)
                }
                
                Section(header: Text("Passengers")) {
                    Stepper(value: $numberOfPassengers, in: 1...10) {
                        Text("Passengers: \(numberOfPassengers)")
                    }
                }
                
                Section(header: Text("Ticket Price")) {
                    Text("$\(ticketPrice, specifier: "%.2f")")
                }
                
                Button(action: {
                    bookTravel()
                    showingConfirmationScreen = true
                }) {
                    Text("Book Travel")
                }
            }
            .navigationTitle("Harry Space")
            .sheet(isPresented: $showingConfirmationScreen) {
                ConfirmationView(isPresented: $showingConfirmationScreen, ticketPrice: $ticketPrice)
            }
        }
    }
    
    private func bookTravel() {
        // Handle the booking logic
        // Calculate ticket price based on selections
        ticketPrice = calculateTicketPrice()
    }
    
    private func calculateTicketPrice() -> Double {
        // Example pricing logic
        var basePrice = 1000.0
        if selectedRocket == "Starship" {
            basePrice += 500.0
        } else if selectedRocket == "New Shepard" {
            basePrice += 300.0
        }
        
        if selectedSeat == "Business" {
            basePrice += 200.0
        } else if selectedSeat == "First Class" {
            basePrice += 500.0
        }
        
        if selectedDestination == "Mars" {
            basePrice += 1000.0
        } else if selectedDestination == "Alpha Centauri" {
            basePrice += 5000.0
        }
        
        return basePrice * Double(numberOfPassengers)
    }
}

struct ConfirmationView: View {
    @Binding var isPresented: Bool
    @Binding var ticketPrice: Double
    
    var body: some View {
        VStack {
            Text("Booking Confirmation")
                .font(.largeTitle)
                .padding()
            
            Text("Your ticket has been booked successfully!")
                .padding()
            
            Text("Total Price: $\(ticketPrice, specifier: "%.2f")")
                .font(.title2)
                .padding()
            
            Button("Done") {
                isPresented = false
            }
            .buttonStyle(.borderedProminent)
            .controlSize(.large)
            .padding()
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}