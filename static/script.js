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
        document.getElementById('debt-list').innerHTML = html

    })

}