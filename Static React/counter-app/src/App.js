import './App.css';
import {useState} from 'react';
import Button from './components/Button';

function App() {
  const [count, setCount] = useState(0); 
  const increase = () => {
    setCount(count+1);
  }
  const decrease = () => {
    setCount(count-1);
  }

  return (
    <div className = "App">
      <h2>Count = {count} </h2>
      <Button task={increase} title = "+"/>
      <Button task={decrease} title = "-"/>
    </div>
  );
}

export default App;