import React,{useState} from 'react'

const Greeting = () => {
    const [state, setState] = useState("world")
    const [formState, setFormState] = useState("world")
    
    const formHandler = (e) =>{
        setFormState(e.target.value);
    }

    const submitHandler = (e) =>{
        e.preventDefault();
        setState(formState);
    }
    return (
        <div>
            <p>Goodbye {state}</p>

            <form onSubmit={submitHandler}>
                <input type='text' name='name' value={formState} onChange={formHandler}/>
                <button type="submit">Submit</button>
            </form>
        
        
        </div>
    )
}

export default Greeting
