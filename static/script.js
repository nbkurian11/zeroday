function loadDebts(){
    fetch('/debts')
    .then(response => response.json())
    .then(data => {
        let html = ''
        data.forEach(debt => {
            html += `
            <div>
            <h3>${debt.name}</h3>
                <p>Balance: $${debt.balance}</p>
                <p>Interest Rate: ${debt.interest_rate}%</p>
                <p>Minimum Payment: $${debt.minimum_payment}</p>
                <p>Payoff Months: ${debt.payoff_months}</p>
                <button onclick="deleteDebt(${debt.id})">Delete</button>
            </div>
            `
        })
        let total = data.reduce((sum, debt) => sum + debt.balance, 0)
        document.getElementById('total').innerText = total.toFixed(2)
        document.getElementById('debt-list').innerHTML = html

    })

}

function deleteDebt(id){
    fetch(`/debts/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        loadDebts()
    })


}

function addDebt(){
    //sends a request to post/ debts endpoint
    fetch(`/debts`, {
        //tells fetch to send a post request instead of default get
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        //converts js object into a json string
        body: JSON.stringify({
            name: document.getElementById('name').value,
            balance: parseFloat(document.getElementById('balance').value),
            interest_rate: parseFloat(document.getElementById('interestrate').value),
            minimum_payment: parseFloat(document.getElementById('minpayment').value)
        })

    })
    .then(response => response.json())
    .then(data => {
        loadDebts()
    })
    
}