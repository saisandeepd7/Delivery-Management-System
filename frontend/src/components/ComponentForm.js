import React, { useState } from 'react';
import axios from 'axios';

const ComponentForm = () => {
    const [name, setName] = useState('');
    const [newPrice, setNewPrice] = useState('');
    const [repairPrice, setRepairPrice] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        const componentData = { name, new_price: newPrice, repair_price: repairPrice };
        await axios.post('http://localhost:8000/api/components/', componentData);
        alert('Component added!');
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>Name:</label>
            <input value={name} onChange={(e) => setName(e.target.value)} />
            <label>New Price:</label>
            <input value={newPrice} onChange={(e) => setNewPrice(e.target.value)} />
            <label>Repair Price:</label>
            <input value={repairPrice} onChange={(e) => setRepairPrice(e.target.value)} />
            <button type="submit">Add Component</button>
        </form>
    );
};

export default ComponentForm;
