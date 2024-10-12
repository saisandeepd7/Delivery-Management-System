import React, { useEffect, useState } from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip } from 'recharts';
import axios from 'axios';

const RevenueGraph = ({ period }) => {
    const [data, setData] = useState([]);

    useEffect(() => {
        axios.get(`http://localhost:8000/api/revenue/${period}/`)
            .then(response => {
                setData(response.data.revenue); // Assuming data comes in { revenue: [] } format
            });
    }, [period]);

    return (
        <LineChart width={600} height={300} data={data}>
            <Line type="monotone" dataKey="revenue" stroke="#8884d8" />
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
        </LineChart>
    );
};

export default RevenueGraph;
