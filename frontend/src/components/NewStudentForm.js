import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewStudentForm extends React.Component {
  state = {
    pk: 0,
    name: "",
    email: "",
    student_id: "",
    grad_year: "",
    hours_remaining: "",
  };

  componentDidMount() {
    if (this.props.student) {
      const { pk, name, email, student_id, grad_year, hours_remaining } = this.props.student;
      this.setState({ pk, name, email, student_id, grad_year, hours_remaining });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createStudent = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editStudent = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.student ? this.editStudent : this.createStudent}>
        <FormGroup>
          <Label for="name">Name:</Label>
          <Input
            type="text"
            name="name"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.name)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="email">Email:</Label>
          <Input
            type="email"
            name="email"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.email)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="document">Student Id:</Label>
          <Input
            type="text"
            name="document"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.student_id)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="phone">Graduation Year:</Label>
          <Input
            type="text"
            name="phone"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.grad_year)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="phone">Hours Remaining:</Label>
          <Input
            type="text"
            name="phone"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.hours_remaining)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewStudentForm;