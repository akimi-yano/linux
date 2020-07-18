import React from 'react';

class ClassExample extends React.Component {
    constructor(){
        super()
        this.state = {
            index:0,
            data:['apple', 'orange', 'oishi']
        }
    }

    componentDidMount(){
        console.log("Component mounted and dom is ready")
        // anything you want to do after dom is fully loaded
    }

    componentWillMount(){
        
    }

    componentWillUpdate(){
        
    }

    buttonHandler (e) {
        this.setState({index:this.state.index === 2 ? 0 : this.state.index + 1})
    }
    
    render(){
        const list = this.state.data.map((item,index) => (
            this.state.index === index ? 
            (<div key={index}>
                Card {item}
            </div>)
            : null
        ))
        return (
        <div>
            {list}
            <button onClick={(e) => this.buttonHandler()}>
                Change
            </button>
        </div>
        )
    }
}

export default ClassExample